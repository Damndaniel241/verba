<script lang="ts" setup>
import { useCurrentRecipient } from '@/stores/currentRecipient';
import { ref,onMounted,onUnmounted,onBeforeMount} from 'vue';
import axios from 'axios';
import { useChatStore } from '@/stores/useChatStore';
import { useRoomStore } from '@/stores/room';
import { useAuthStore } from '@/stores/auth';

const currentRecipient = useCurrentRecipient();
const chat = useChatStore();
const roomId = ref<string>("");
const room = useRoomStore();
const auth = useAuthStore();


roomId.value = room.currentRoomId;
async function createRoomId(){
  try{
  const response = await axios.post("http://127.0.0.1:8000/chat/create-room-id/",{
    recipient_id:currentRecipient.recipientObj.id
  },{
    headers:{
      Authorization:`JWT ${auth.access_token}`
    }
  });
  roomId.value = response.data.data.id;
  room.currentRoomId = response.data.data.id;

  console.log("Current recpient baby ",currentRecipient.recipientObj);
  
  console.log("roomID = ",roomId.value);
  chat.connect(response.data.data.id,auth.access_token)

  

  }catch(err){
    console.error("err creating room id ",err)
  }
}

// const props = defineProps({
//   roomObj:Object
// });


// onBeforeMount(async()=>{
//    await createRoomId();
//   //  chat.connect(roomId.value,auth.access_token);
// })
const newMessage = ref('')


function handleSend() {
  console.log("handleSend was clicked");
    console.log("user id00000000 number  18 = ",auth.userId);
  console.log("in message list this is roomID = ",room.currentRoomId );
  console.log("current recipient id = ",currentRecipient.recipientObj.id);
  console.log(`is user id(${auth.userId}) same as recipient(${currentRecipient.recipientObj.id}) ? = `, auth.userId !== currentRecipient.recipientObj.id);
  
  
  // didYouSend.value = true;
  const content = newMessage.value.trim();
  if (!content) return;
  chat.sendMessage(content); // ⬅️ Actually send to WebSocket
  newMessage.value = '';
  
  // didYouSend.value = false;
}



onUnmounted(() => {
  chat.disconnect()
})
</script>

<template>
    <!-- <div class="">
    <h1>current recipient</h1>
    <p>id: {{ currentRecipient.recipientObj.id }}</p>
    <p>user_name: {{ currentRecipient.recipientObj.user_name }}</p>
    <p>email: {{ currentRecipient.recipientObj.email }}</p>

    <p>{{ currentRecipient.recipientObj.roomId }}</p>
    <p v-if="auth.access_token">{{ auth.access_token }}</p>
    </div> -->

     <div class="col-span-3 flex flex-col relative ">
      <div class="h-[2.5em] text-[1.8em] font-bold">
         {{ currentRecipient.recipientObj.user_name }}
      </div>
      <div class="overflow-y-scroll max-h-120 ">

   <div v-for="(msg, index) in chat.messages" :key="index" class="">
    <!-- left side -->
        <div v-if="msg.sender == currentRecipient.recipientObj.user_name" class="flex gap-3 items-end">  
           <div class="">
        <img class="h-8 w-8 rounded-full object-cover" src="https://randomuser.me/api/portraits/women/87.jpg">
    </div>
    <div  class="flex flex-col gap-1">
        <h1 class="text-[#424548] text-[0.63em] ">{{ msg.sender }}</h1>
        <div class="bg-[#F0F2F5] p-2 max-w-[100%] rounded-[0.3em]">{{ msg.message }}</div>
    </div>
      </div>

      <!-- right side -->
       <div v-else  class="flex gap-3 items-end justify-self-end">
         
    <div class="flex flex-col gap-1">
        <h1 class="text-[#424548] text-[0.63em] text-end ">{{ msg.sender }}</h1>
        <div class="bg-[#F0F2F5] p-2 rounded-[0.3em]">{{ msg.message }}  </div>
    </div>
      <div class="">
        <img class="h-8 w-8 rounded-full object-cover" src="https://randomuser.me/api/portraits/women/87.jpg">
    </div>
      </div>


    </div>
      </div>

       <div class="absolute bottom-0 left-0 right-0 flex-1 pb-[2.5em] overflow-y-auto">
     <!-- starts here -->
       <div class="flex gap-2 items-center">
    <div class="">
      <img
        class="h-8 w-8 rounded-full object-cover"
        src="https://randomuser.me/api/portraits/women/87.jpg"
      />
    </div>
    <div class="flex flex-1 bg-[#F0F2F5] items-center">
    <input v-model="newMessage" @keyup.enter="handleSend()" class="w-full focus-within:outline-none h-[3em]" type="text" placeholder="Type a message">
    <span @click="handleSend()" class="pi pi-send rotate-45 me-3 cursor-pointer" style="font-size: 2em"></span>
    </div>
  </div>
      <!-- <MessageInput @send="handleSend()" /> -->
      <!-- ends here -->
    </div>


     </div>


</template>