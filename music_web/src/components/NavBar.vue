<template>
    <nav class="navbar navbar-expand-lg bg-body-tertiary bg-primary" data-bs-theme="dark">
        <div class="container-fluid">
            <router-link class="navbar-brand" :to="{name:'main_page_view'}">Music Web</router-link>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarText">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                <li class="nav-item">
                    <router-link class="nav-link" active-class="active" :to="{name:'main_page_view'}">主页</router-link>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Features</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Pricing</a>
                </li>
                <li class="nav-item serach">
                    <input class="form-control me-2" type="search" placeholder="请输入想要查找的内容" aria-label="Search">
                </li>
                <li class="nav-item serach-btn">
                    <button class="btn btn btn-primary" type="submit">搜索</button>
                </li>
            </ul>





            <ul class="navbar-nav" v-if="$store.state.user.is_login">
                <li class="nav-item dropdown">
                  <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                    {{ $store.state.user.username }}
                  </a>
                  <ul class="dropdown-menu">
                    <li><router-link :to='{name:"user_account_userinfo"}' class="dropdown-item">我的个人信息</router-link></li>
                    <li><hr class="dropdown-divider"></li>
                    <li><a class="dropdown-item" href="#" @click="logout">退出</a></li>
                  </ul>
                </li>
            </ul>
            <ul class="navbar-nav" v-else-if="!$store.state.user.polling_info">
                <div class="account" >
                    <span class="navbar-text login-btn">
                    <button  class="btn btn-outline-success me-2" type="button">
                        <router-link  :to="{name: 'user_account_login'}">登录</router-link>
                    </button>   
                        </span>
                    <span class="navbar-text register-btn">
                        <button  class="btn btn-outline-success me-2" type="button">
                            <router-link :to="{name: 'user_account_register'}">注册</router-link>
                        </button> 
                    </span>
                </div>
            </ul>
        
            
        </div>
        </div>
    </nav>
</template>

<script>
import { useStore } from 'vuex';
export default{
    setup(){
        const store = useStore()
        const logout = () =>{
            store.dispatch("logout")
            
        }
        return{
            logout,
        }

    }

}
</script>


<style scoped>
.serach{
    margin-left: 40px;
    

}
.serach-btn{
    margin-left: 20px;
    transition: transform 0.5s cubic-bezier(0.68, -0.55, 0.27, 1.55); /* 调整过渡时间和缓动函数 */
    transition-delay: 0.2s;
}
.serach-btn:hover{
    cursor: pointer;
    color: black;
    transform: scale(1.3); /* 按钮放大到原始尺寸的1.1倍 */
    
}
.active{
    color: blue; /* 例如，将激活状态的链接文本颜色设置为红色 */
    font-weight: bold; /* 设置字体加粗等 */
}
</style>