import { ref, computed,watch } from 'vue'
import { defineStore } from 'pinia'


export const useRoomStore = defineStore('room',()=>{

    const currentRoomId = ref("");

    function setCurrentRoomId(id:string){
      currentRoomId.value = id;
    }


    watch(currentRoomId,(newCurrentRoomId,oldCurrentRoomId)=>{
            console.log("room Id changed to ",newCurrentRoomId);
            
        });

    return {currentRoomId,setCurrentRoomId}
},
{
  persist: true   // ✅ this tells Pinia to persist the store
},
);