import { createRouter, createWebHistory } from 'vue-router'
import UserAccountLoginView from '@/views/user/account/UserAccountLoginView'
import UserAccountRegisterView from '@/views/user/account/UserAccountRegisterView'
import MainPageView from '@/views/MainPageView'

const routes = [
    {
        path:'/user/account/login',
        name:'user_account_login',
        component:UserAccountLoginView, 
        meta: {
          requestAuth : false,
        },
    },
    {
        path:'/user/account/register',
        name:'user_account_register',
        component:UserAccountRegisterView, 
        meta: {
          requestAuth : false,
        },
    },
    {
        path:'/main_page',
        name:'main_page_view',
        component:MainPageView, 
        meta: {
          requestAuth : true,
        },
    },

]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
