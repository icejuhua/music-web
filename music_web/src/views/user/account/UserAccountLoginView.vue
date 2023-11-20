<template> 
    <div class="container-fluid container">
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
      <div class="col-sm-6 col-md-4">
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
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
//import $ from 'jquery';
import axios from 'axios';

export default{
  setup(){
    let username = ref('')
    let password = ref('')
    const login = () =>{
      console.log("sending login info"),
      axios.post("http://101.43.45.110:8000/login_test/",{
        username:username.value,
        password:password.value,
      })
      .then(resp =>{
        console.log(resp.data.error_msg);
      })
      .catch(resp =>{
        console.log(resp.error_msg);
      })
        // $.ajax({
        //   url : "http://101.43.45.110:8000/login_test/",
        //   type:'post',
        //   data:{
        //     username:username.value,
        //     password:password.value,
        //   },
        //   success(resp){
        //     console.log("login success")
        //     console.log(resp)
        //   },
        //   error(resp){
        //     console.log(resp)
        //   }

        // })
    };
    return{
      login,
      username,
      password,
    }

  }
}

</script>


<style scoped>
.container-fluid{
  
  /* margin: 0%; */
  height: 100vh;
}
.logo-container{
  width: 100%; /* 使图片宽度填满容器 */
  height: 100%; /* 使图片高度填满容器 */
  
}
.login-form{
  margin-top: auto;
  margin-bottom: auto;
}
.login-row{
  height: 100vh;
  text-align: center;

}
</style>