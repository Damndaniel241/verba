import { ref, computed } from 'vue'
import { defineStore } from 'pinia'


export const useRoomStore = defineStore('room',()=>{

    const currentRoomId = ref("");

    return {currentRoomId}
},
{
  persist: true   // ✅ this tells Pinia to persist the store
},
);