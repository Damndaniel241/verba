import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { jwtDecode } from "jwt-decode";
import axios from 'axios';


export const useAuthStore = defineStore('auth',()=>{
    const access_token = ref("");
    // const isLoggedIn = ref<boolean>(false)
    const owner = ref({}); 
     const isAuthenticated = computed(() => !!access_token.value)




   

     const userId = computed(()=>{
         if (!access_token.value) return null
         try{
           const decoded:any = jwtDecode(access_token.value);
           return decoded.user_id || null
         }
    catch(e){
        return null
    } 

     })



          async function getUser(){
  try{
    if(userId){
    const response = await axios.get(`http://127.0.0.1:8000/user/${userId}`);
    owner.value = response.data.data}
  }catch(error){
    console.error("error retreiving user", error)
  }
}

getUser();



    function clearToken(){
        access_token.value = "";
      
    }

    return {access_token,isAuthenticated,userId,owner, clearToken}
},

{
  persist: true   // ✅ this tells Pinia to persist the store
},

);