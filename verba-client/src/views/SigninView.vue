<script setup lang="ts">
import axios from 'axios'
import { ref } from 'vue'
import Header from '@/components/Header.vue'
import { useAuthStore } from '@/stores/auth'
import { storeToRefs } from 'pinia'
import { useRouter } from 'vue-router'

const router = useRouter()

const email = ref<string>('')
const password = ref<string>('')
const auth = useAuthStore()
const { access_token } = storeToRefs(auth)

console.log("signin isLoggedIn =",auth.isAuthenticated );


async function signin() {
  const formData = {
    email: email.value,
    password: password.value,
  }
  try{
  const response = await axios.post('http://127.0.0.1:8000/user/signin/', formData)
  console.log('response.data access= ', response.data.data.tokens.access)
  access_token.value = response.data.data.tokens.access
  router.push({ name: 'chatLayout' })
  }catch(error){
    console.error("signin went wrong",error);
  }
}
</script>

<template>
  <Header />
  <div class="h-screen">
    <div class="flex justify-content-center items-center flex-col text-[1.2em]">
      <h1 class="text-center text-[1.4em]">Create your account</h1>
      <div class="flex flex-col gap-3">
        <div class="flex flex-col gap-1">
          <label>email</label>
          <input
            class="bg-[#F1F2F4] h-[2em] rounded-[0.9em] placeholder:ms-[1em] placeholder:text-sm focus-within:outline-none"
            type="email"
            placeholder="Email"
            v-model="email"
          />
        </div>
        <div class="flex flex-col gap-1">
          <label>Password</label>
          <input
            class="h-[2em] bg-[#F1F2F4] rounded-[0.9em] placeholder:ms-[5em] placeholder:text-sm focus-within:outline-none"
            type="password"
            placeholder="Password"
            v-model="password"
          />
        </div>

        <button
          @click="signin()"
          class="bg-[#DCE8F3] h-[2.2em] rounded-[0.9em] cursor-pointer text-black"
        >
          Sign in
        </button>
      </div>
      <RouterLink :to="{ name: 'signup' }" class="text-sm mt-4 hover:underline"
        >Don't have an account?sign up</RouterLink
      >
    </div>
  </div>
</template>
