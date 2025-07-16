<script setup lang="ts">
import axios from 'axios'
import { useAuthStore } from '@/stores/auth'

import { storeToRefs } from 'pinia'
import { useRouter } from 'vue-router'

const router = useRouter()

const auth = useAuthStore()


async function logout() {
  try {
    const response = await axios.post(
      'http://127.0.0.1:8000/user/logout/',
      {},
      {
        headers: {
          Authorization: `JWT ${auth.access_token}`,
        },
        withCredentials: true,
      },
    )
    console.log('logout response data = ', response.data)
    auth.clearToken()
   await router.push({ name: 'signin' })
  } catch (error) {
    console.error('error logging out', error)
  }
}

</script>

<template>
    <div class="flex justify-between items-center mx-[1em]">
    <h1 class="text-[1.5em] text-black ">Verba</h1>
    <!-- <span class="pi pi-cog"></span> -->
       <button v-show="auth.isAuthenticated" @click="logout()" class="text-white bg-red-500 rounded-[20px] text-[0.9em] p-[0.5em] cursor-pointer">
      logout
    </button>
    </div>
</template>