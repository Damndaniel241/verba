<script setup lang="ts">
import axios from 'axios'
import Header from '@/components/Header.vue'
import { AvatarFallback, AvatarImage, AvatarRoot } from 'radix-vue'
import SidebarChatList from './SidebarChatList.vue'
import MessageList from './MessageList.vue'
import MessageList2 from './MessageList2.vue'
import BlankVerba from '@/components/BlankVerba.vue'
import { useClickedPages } from '@/stores/clickedpages'
import { storeToRefs } from 'pinia'
import { useAuthStore } from '@/stores/auth'
import { watch } from 'vue'
import { useChatStore } from '@/stores/useChatStore'
import { useRoute } from 'vue-router'


const clickedpages = useClickedPages();
const auth = useAuthStore();
const chat = useChatStore();
const route = useRoute();



// watch(
//   () => route.params.roomId,
//   (newRoomId) => {
//     if (newRoomId) {
//       chat.connect(newRoomId as string, auth.access_token)
//     }
//   },
//   { immediate: true }
// )

// auth.$subscribe((state, prevState) => {
//   console.log('Count changed from', prevState.access_token, 'to', state.access_token)
// }, { detached: true })
const {blankVerbaIsPresent} = storeToRefs(clickedpages)

// console.log("chatLayout isLoggedIn = ",auth.isAuthenticated );
</script>

<template>
  <Header />
  <div class="grid grid-cols-4 h-screen ">
<SidebarChatList/>
<BlankVerba v-if="blankVerbaIsPresent"/>
<!-- <MessageList v-else/> -->
<MessageList2 v-else/>
  </div>
  <!-- <div class="grid grid-flow-col grid-rows-3 h-screen">
  <div class="row-span-3 col-span-1  bg-red-500">01</div>
  <div class="col-span-3 bg-green-500">02</div>
  <div class="col-span-2 row-span-2">03</div>
</div> -->
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap');

body {
  font-family: 'Inter', sans-serif;
}
</style>
