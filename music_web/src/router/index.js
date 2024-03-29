import { createRouter, createWebHistory } from 'vue-router'
import UserAccountLoginView from '@/views/user/account/UserAccountLoginView'
import UserAccountRegisterView from '@/views/user/account/UserAccountRegisterView'
import MainPageView from '@/views/MainPageView'
import UserInfoView from '@/views/user/account/UserInfoView'
import store from '@/store/index'
import MyFavoriteMusicView from '@/views/MyFavoriteMusicView'
import MusicInfoView from '@/views/music/MusicInfoView'

const routes = [
    {
        path:"/user/myfavorite-music",
        name:'favorite_music',
        component:MyFavoriteMusicView,
        meta:{
            requestAuth:true
        }
    },
    {
        path:'/music/music-info',
        name:"music_info",
        component:MusicInfoView,
        meta: {
          requestAuth:true
        },
    },
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
    {
        path:'/user/account/userinfo',
        name:'user_account_userinfo',
        component:UserInfoView,
        meta:{
            requestAuth : true,
        }
    }

]

const router = createRouter({
  history: createWebHistory(),
  routes
})
router.beforeEach((to , from ,next) => {
    if(to.meta.requestAuth && !store.state.user.is_login){
      next({name : 'user_account_login'});
    } else{
      next();
    }
  })
export default router
