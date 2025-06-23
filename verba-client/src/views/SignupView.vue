<script setup lang="ts">
import axios from 'axios'
import Header from '@/components/Header.vue'
import { useAuthStore } from '@/stores/auth';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const email = ref<string>("");
const user_name = ref<string>("");
const password = ref<string>("");
const password2 = ref<string>("");


// const auth = useAuthStore();

// console.log("access token ooo = ",auth.access_token);

const router = useRouter();

async function signup() {
  const formData={
    user_name :user_name.value,
    email: email.value,
    password:password.value,
    password2:password2.value,

  }
try{
  const response = await axios.post("http://127.0.0.1:8000/user/signup/", formData)
  router.push({name:"signin"})
}catch(error){
  console.error("something went wrong",error);
}
}



</script>

<template>
  <div class="h-screen">
    <Header />
    <div class="flex justify-content-center items-center flex-col text-[1.2em]">
      <h1 class="text-center text-[1.4em]">Create your account</h1>
      <div class="flex flex-col gap-3">
        <div class="flex flex-col gap-1">
          <label>email</label>
          <input
          v-model="email"
            class="bg-[#F1F2F4] h-[2em] rounded-[0.9em] placeholder:ps-[1em]"
            type="email"
            placeholder="Email"
          />
        </div>
        <div class="flex flex-col gap-1">
          <label>username</label>
          <input
          v-model="user_name"
            class="h-[2em] bg-[#F1F2F4] rounded-[0.9em] placeholder:ps-[1em]"
            type="text"
            placeholder="username"
          />
        </div>
        <div class="flex flex-col gap-1">
          <label>Password</label>
          <input
          v-model="password"
            class="h-[2em] bg-[#F1F2F4] rounded-[0.9em] placeholder:ps-[1em] text-sm"
            type="password"
            placeholder="password"
          />
        </div>
        <div class="flex flex-col gap-1">
          <label>enter Password again</label>
          <input
          v-model="password2"
            class="h-[2em] bg-[#F1F2F4] rounded-[0.9em] placeholder:ps-[1em] text-sm"
            type="password"
            placeholder="retype Password"
          />
        </div>
        <button @click="signup()" class="bg-[#DCE8F3] h-[2.2em] rounded-[0.9em] cursor-pointer text-black">
          Sign up
        </button>
      </div>
      <RouterLink :to="{ name: 'signin' }" class="text-sm mt-4 hover:underline"
        >Already have an account?sign in</RouterLink
      >
    </div>
  </div>
</template>
