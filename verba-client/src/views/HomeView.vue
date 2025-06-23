<script setup lang="ts">
import Header from '@/components/Header.vue'
import axios from 'axios'
import { useAuthStore } from '@/stores/auth'
// import { VueCookies } from 'vue-cookies';
import { storeToRefs } from 'pinia'
import { useRouter } from 'vue-router'

// const $cookies = inject<VueCookies>('$cookies');
// $cookies.get("") st

const router = useRouter()

const auth = useAuthStore()

// const {access_token} = storeToRefs(auth);

console.log(auth.access_token)

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
    // console.log('logout response data = ', response.data)
    auth.clearToken()
    router.push({ name: 'signin' })
  } catch (error) {
    console.error('error logging out', error)
  }
}
</script>

<template>
  <Header />

  <div class="">
    <button @click="logout()" class="text-white bg-red-500 rounded-2 p-3 cursor-pointer">
      logout
    </button>
  </div>
</template>
