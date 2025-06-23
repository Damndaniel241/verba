import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import { storeToRefs } from 'pinia'
import { useAuthStore } from '@/stores/auth'
import SigninView from '@/views/SigninView.vue'



// const { isAuthenticated } = storeToRefs(auth);

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue'),
    },
    {
      path: '/signup',
      name: 'signup',
      component: () => import('@/views/SignupView.vue'),
    },
    {
      path: '/signin',
      name: 'signin',
      component: SigninView,
    },
    {
      path: '/verba',
      name: 'chatLayout',
      component: () => import('@/views/ChatLayout.vue'),
      meta: { requiresAuth: true },
    },
    {
      path: '/sidebar',
      name: 'SidebarChatList',
      component: () => import('@/views/SidebarChatList.vue'),
    },
    {
      path: '/chat',
      name: 'MessageList',
      component: () => import('@/views/MessageList.vue'),

    },
    {
      path: '/chat2',
      name: 'MessageList2',
      component: () => import('@/views/MessageList2.vue'),

    },

    {
      path: '/test',
      name: 'TestDoc',
      component: () => import('@/views/TestDocView.vue'),
    },

  ],
})

router.beforeEach((to, from) => {

  const auth = useAuthStore();

  if (to.meta.requiresAuth && !auth.isAuthenticated ) {
    return { name: 'signin' }
  } 
})

export default router
