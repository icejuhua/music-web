import { createRouter, createWebHistory } from 'vue-router'
import UserAccountLoginView from '@/views/user/account/UserAccountLoginView'

const routes = [
  {
    path:'/user/account/login',
    name:'user_account_login',
    component:UserAccountLoginView,
   
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
