
<script setup lang="ts">
import { ref, onMounted } from 'vue'
// import socket from '@/socket' // adjust path based on where you import your socket instance

const messages = ref<string[]>([])
const newMessage = ref('')


const emit = defineEmits<{
  (e: 'send', content: string): void
}>()



function handleSend() {
  if (!newMessage.value.trim()) return
  emit('send', newMessage.value.trim())
  newMessage.value = ''
}



// onMounted(() => {
//   socket.on('message', (message: string) => {
//     messages.value.push(message)
//   })
// })

// function sendMessage() {
//   if (newMessage.value.trim() !== '') {
//     socket.emit('message', newMessage.value)
//     newMessage.value = ''
//   }
// }
</script>


<template>
 
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

</template>
