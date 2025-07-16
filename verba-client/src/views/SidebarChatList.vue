<script setup lang="ts">
import { useAuthStore } from '@/stores/auth';
import axios from 'axios';
import { onMounted, onUnmounted,ref } from 'vue';
import { useClickedPages } from '@/stores/clickedpages'
import { storeToRefs } from 'pinia'
import { useCurrentRecipient } from '@/stores/currentRecipient';
import { useChatStore } from '@/stores/useChatStore';
import { useRouter,useRoute } from 'vue-router';
import { useRoomStore } from '@/stores/room';
const clickedpages = useClickedPages();

const router = useRouter();
const route = useRoute();
const room = useRoomStore();
const roomId = ref<string>("");

const {blankVerbaIsPresent} = storeToRefs(clickedpages);
// const {changeBlankVerba} = storeToRefs(clickedpages);
let currentRecipient = useCurrentRecipient();


const auth = useAuthStore();
const chat = useChatStore();

console.log("the current recipient =",currentRecipient);


async function createRoomId(recipient:number){
  try{
  const response = await axios.post("http://127.0.0.1:8000/chat/create-room-id/",{
    recipient_id:recipient
  },{
    headers:{
      Authorization:`JWT ${auth.access_token}`
    }
  });
  // roomId.value = response.data.data.id;
  // room.currentRoomId = response.data.data.id;

  // room.setCurrentRoomId(response.data.data.id);
  // console.log("Current recpient baby ",currentRecipient.recipientObj);
  
  console.log("roomID = ",roomId.value);
  // chat.connect(roomId.value,auth.access_token)


  return response.data.data.id;

  }catch(err){
    console.error("err creating room id ",err)
  }
}

   function changeBlankVerba(userObj:{}){
     blankVerbaIsPresent.value = false;
    // createRoomId();

        // update route param *without* reloading component
  // router.replace({
  //   name: route.name as string, // 'Chat' or whatever you named the route
  //   params: {
  //     // ...route.params,
  //     roomId: roomId.value,
  //   },
  // })

  // await router.push({name:"MessageList",params:{roomId:room.currentRoomId}})
      // currentRecipient.selectRecipient(userObj)
      
    }

  // createRoomId();

    


let userList = ref<[]>([]);

 function getRecipientObj(userObj:{},roomID:string){
  // createRoomId();
  if (chat.socket?.onopen){
  chat.disconnect();
  }
   blankVerbaIsPresent.value = false;
  currentRecipient.selectRecipient(userObj);
  console.log("ihave gotten recipient id oooo = ",userObj);
    console.log("therefore recipient id is ",currentRecipient.recipientObj.id);
    
    chat.connect(roomID,auth.access_token)

  //     const response = await axios.post("http://127.0.0.1:8000/chat/create-room-id/",{
  //   recipient_id:currentRecipient.recipientObj.id
  // },{
  //   headers:{
  //     Authorization:`JWT ${auth.access_token}`
  //   }
  // });
  //  room.setCurrentRoomId(response.data.data.id);
  //   chat.connect(response.data.data.id,auth.access_token)
  
}


async function getUsers(){
  try{
    const response = await axios.get("http://127.0.0.1:8000/user/users/");
    userList.value = response.data.data
    console.log("users list old = ",userList.value);
    for (let userObj of userList.value){
      const roomIdForObj = await createRoomId(userObj.id);
      userObj.roomId = roomIdForObj;
      currentRecipient.recipientObj.roomId = roomIdForObj;
      
    }

    console.log("users list new = ",userList.value);
    
    
  }catch(error){
    console.log("error retreiving all users", error)
  }
}

getUsers();

// const prf = [1,2,3,4];
</script>


<template>
        <div class="flex flex-col gap-3 mx-4">
      <h1 class="text-[1.4em]">Chats</h1>
      <div class="flex justify-content-center items-center bg-[#F0F2F5] gap-2 rounded-[0.3em]">
        <span class="pi pi-search ms-2"></span>
        <input class="h-[2.4em] focus-within:outline-none" type="text" placeholder="Search" />
      </div>
      <div v-show="auth.userId !== item.id" v-for="item in userList" :key="item.user_name"  @click="getRecipientObj(item,item.roomId)"  class="flex items-center gap-3 hover:bg-[#F0F2F5] cursor-pointer">
       <div class="">
        <img class="h-14 w-14 rounded-full object-cover" src="https://randomuser.me/api/portraits/women/87.jpg">
    </div>

        <div class="flex flex-col">
          <h1 class="text-[#424548] text-md ">{{ item.user_name }}</h1>
          <h1 class="text-[#A9B4BF] text-sm">see you tommorow</h1>
        </div>
      </div>
    </div>
</template>