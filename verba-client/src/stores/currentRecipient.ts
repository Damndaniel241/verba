import { ref, computed,watch } from 'vue'
import { defineStore } from 'pinia'

export const useCurrentRecipient = defineStore('currentRecipient',()=>{
    // const recipientName = ref<string>("");
    const recipientObj = ref<any>({});
    function selectRecipient(name:{}){
        // recipientName.value = name
        recipientObj.value = name
        // console.log("yayyyy i was clicked from current recipient store");
        
    }

    watch(recipientObj,(newrecipientObj,oldrecipientObj)=>{
        console.log("recipient Obj changed to ",newrecipientObj);
        
    });


    return {recipientObj, selectRecipient}
})