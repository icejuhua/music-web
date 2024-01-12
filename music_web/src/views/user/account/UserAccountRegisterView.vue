<template>
    <ContentField>
        <div class="main-page">
            <form @submit.prevent="register" class="row g-3 ">
                <div class="col-md-6">
                    <label for="username" class="form-label">账号*</label>
                    <input v-model="username" type="text" class="form-control" id="username">
                </div>
                <div class="col-md-6">
                    <label for="name" class="form-label">昵称*</label>
                    <input v-model="name" type="text" class="form-control" id="name">
                </div>
                <div class="col-12">
                    <label for="inputPassword" class="form-label">密码*</label>
                    <input v-model="password" type="password" class="form-control" id="password" placeholder="密码无要求">
                </div>
                <div class="col-12">
                    <label for="password_confirm" class="form-label">确认密码*</label>
                    <input v-model="password_confirm" type="password" class="form-control" id="password_confirm" placeholder="请确认密码一致">
                </div>
                <div class="col12">
                    <div class="mb-3">
                        <label for="info" class="form-label">自我介绍</label>
                        <textarea v-model="info" class="form-control" id="infp" rows="4"  placeholder="可不填"></textarea>
                    </div>
                </div>
                <div class="error-message">{{ error_message }}</div>
                <div class="col-12">
                    <button type="submit" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#staticBackdrop">注册</button>
                </div>
                <ModelComponents :error_msg="正在注册"/>
                
                
                
            </form>
        </div>
    </ContentField>
    
</template>

<script>
import ContentField from '@/components/ContentField.vue'
import { ref } from 'vue'
import axios from 'axios'

import ModelComponents from '@/components/ModelComponents.vue'
export default{

    components:{
            ContentField,
            ModelComponents,
        },
    
    setup(){
        let username = ref("")
        let name = ref("")
        let password = ref("")
        let password_confirm = ref("")
        let info = ref("")
        let error_message = ref("")
        const register = () =>{
            error_message.value = ""
        
            axios.post("http://101.43.45.110:8000/api/settings/register/",{
                username:username.value,
                name:name.value,
                password:password.value,
                password_confirm : password_confirm.value,
                info : info.value,
            })
            .then(resp=>{
                console.log(resp)
                if(resp.data != "success"){
                    error_message.value = resp.data.error_msg
                    
                }
            })
            .catch(resp=>{
                console.log(resp)
                error_message.value = "错误"
                
            })   
        };
        
        return{
            username,
            name,
            password,
            password_confirm,
            info,
            error_message,
            register,
        }
    },


}


</script>


<style scoped>
.content-feild{
    background-color: rgba(255, 255, 255, 0.5);
}
.main-page{
    background-color: rgba(255, 255, 255, 0.7); /* 使用 rgba 表示半透明度，最后一个参数是透明度，取值范围为 0 到 1 */
    padding: 20px; /* 可选：添加内边距以提高可读性 */
}
.error-message{
    color:red;
}


</style>