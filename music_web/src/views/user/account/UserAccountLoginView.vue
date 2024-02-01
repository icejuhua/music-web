<template> 
    <div class="container-fluid container" v-if="!$store.state.user.polling_info">
    <div class="row login-row">
      <!-- 左侧区域 -->
      <div class="col-sm-6 col-md-8 left-section">
        <!-- 放置Logo和背景图片等内容 -->
        <div class="logo-container">
          <img src="../../../assets/img/th.jpg" alt="Logo" >
          <!-- 其他左侧内容 -->
        </div>
      </div>
      <!-- 右侧登录区域 -->
      <div class="col-sm-6 col-md-4 login-block">
        <form @submit.prevent="login" class="login-form">
          <h2 class="mb-3 text-info p-3">用户登录</h2>
          <div class="mb-3">
            <label for="username" class="form-label">用户名：</label>
            <input v-model="username" type="text" class="form-control" id="username">
          </div>
          <div class="mb-3">
            <label for="password" class="form-label">密码：</label>
            <input v-model="password" type="password" class="form-control" id="password" >
          </div>
          <button type="submit" class="btn btn-primary">登录</button>
          <div style="color: red;">{{ error_msg }}</div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
import { useStore } from 'vuex';
import router from '@/router';
//import $ from 'jquery';


export default{
  components:{
       
    },
  setup(){
    let username = ref('')
    let password = ref('')
    let error_msg = ref('')
    const store = useStore()

    const jwt_token = localStorage.getItem("access_token")
    
    if(jwt_token){
        store.commit("updataAccess",jwt_token);
        store.dispatch('getinfo',{
            success(){
                router.push({name:"main_page_view"})
                store.commit("updataPullinginfo",false)
            },  
            error(resp){
                console.log(resp)
                store.commit("updataPullinginfo",false)
            }
        })
    }

    const login = () =>{
        store.dispatch("login",{
            username:username.value,
            password:password.value,
            success(){
                store.dispatch('getinfo',{
                    success(){
                        window.alert("登录成功")
                        router.push({name:"main_page_view"})
                    },
                    error(resp){
                        error_msg.value = '登录失败'
                        console.log(resp)
                    }
                })
            },
            error(resp){
                error_msg.value = '登录失败'
                console.log(resp)
            }
        })
    }
      
    return{
      login,
      username,
      password,
      error_msg,
      
    }

    }
}


</script>


<style scoped>
.login-block{
  background-color: rgba(204, 189, 189, 0.5);
  height: 400px;
}
.container-fluid{
  
  /* margin: 0%; */
  margin-top: 15vh;
}
.login-row{
  text-align: center;

}
</style>