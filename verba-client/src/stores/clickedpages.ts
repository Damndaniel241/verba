import { ref, computed, watch } from 'vue'
import { defineStore } from 'pinia'

export const useClickedPages = defineStore('clickedpages',()=>{
    const blankVerbaIsPresent = ref<boolean>(true);

    watch(blankVerbaIsPresent,(newBlankVerbaIsPresent,oldBlankVerbalIsPresent)=>{
        console.log("blank changed",blankVerbaIsPresent)
    })


    // function changeBlankVerba(){
    //     blankVerbaIsPresent.value = !blankVerbaIsPresent.value;
    // }
    return { blankVerbaIsPresent }
})