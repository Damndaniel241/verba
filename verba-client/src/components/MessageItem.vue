<script setup lang="ts">


 const props = defineProps({
     isLeftAligned: Boolean,
     messenger:String,
     content:String
   });

</script>

<template>
     <div v-if="isLeftAligned" class="flex gap-3 items-end">
           <div class="">
        <img class="h-8 w-8 rounded-full object-cover" src="https://randomuser.me/api/portraits/women/87.jpg">
    </div>
    <div class="flex flex-col gap-1">
        <h1 class="text-[#424548] text-md ">{{ props.messenger }}</h1>
        <div class="bg-[#F0F2F5] p-2 rounded-[0.3em]">{{ props.content }} </div>
    </div>
      </div>


         <div v-else class="flex gap-3 items-end justify-self-end">
         
    <div class="flex flex-col gap-1">
        <h1 class="text-[#424548] text-md text-end ">{{ props.messenger }}</h1>
        <div class="bg-[#F0F2F5] p-2 rounded-[0.3em]">{{ props.content }} </div>
    </div>
      <div class="">
        <img class="h-8 w-8 rounded-full object-cover" src="https://randomuser.me/api/portraits/women/87.jpg">
    </div>
      </div>
</template>