<script setup lang="ts">
import MessageItem from '@/components/MessageItem.vue'
import { ref, onMounted,onUnmounted } from 'vue'
import MessageInput from '@/components/MessageInput.vue'
import { useCurrentRecipient } from '@/stores/currentRecipient';
import { useRoute } from 'vue-router';
import { useChatStore } from '@/stores/useChatStore';
import { useAuthStore } from '@/stores/auth';
import { useRoomStore } from '@/stores/room';

const currentRecipient = useCurrentRecipient();
const chat = useChatStore();
const userObj = ref({});
const auth = useAuthStore();
const room = useRoomStore();
const didYouSend = ref<boolean>(false);



const route = useRoute()
// const roomId = route.params.roomId as string
// const roomId = currentRecipient.recipientObj["roomID"]


// const roomId = room.currentRoomId

// console.log("in message list this is roomID", currentRecipient.recipientObj);
// console.log("in message list this is roomID", roomId);


 onMounted(async()=>{
  console.log("user id  00000000 number  = ",auth.userId);
  console.log("in message list this is roomID = ",room.currentRoomId );
  console.log("current recipient id = ",currentRecipient.recipientObj.id);
  
//   const accessToken = auth.access_token;
//    chat.connect(roomId,accessToken)
})


onUnmounted(() => {
  chat.disconnect()
})

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
</script>

<template>
  <div class="col-span-3 flex flex-col relative ">
    <div class="h-[2.5em] text-[1.8em] font-bold">{{ currentRecipient.recipientObj.user_name }}</div>

    <div class="overflow-y-scroll max-h-120 ">
     
      <!-- <MessageItem is-left-aligned /> -->
      <!-- <MessageItem/> -->
      <!-- {{ msg.message }} -->
      <!-- <MessageItem  is-left-aligned="auth.userId != currentRecipient.recipientObj.id" messenger={{ currentRecipient.recipientObj.user_name }} content={{ msg.message }} />
      <MessageItem content={{ msg.message }} /> -->
      
      <div v-for="(msg, index) in chat.messages" :key="index" class="">
        <div v-if="!didYouSend" class="flex gap-3 items-end">
           <div class="">
        <img class="h-8 w-8 rounded-full object-cover" src="https://randomuser.me/api/portraits/women/87.jpg">
    </div>
    <div class="flex flex-col gap-1">
        <h1 class="text-[#424548] text-md ">{{ currentRecipient.recipientObj.user_name }}</h1>
        <div class="bg-[#F0F2F5] p-2 rounded-[0.3em]">{{ msg.message }}</div>
    </div>
      </div>

       <div v-else class="flex gap-3 items-end justify-self-end">
         
    <div class="flex flex-col gap-1">
        <h1 class="text-[#424548] text-md text-end ">{{ msg.sender }}</h1>
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
