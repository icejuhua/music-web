<template>
    <ContentField>
        <div class="main-page">
            <form class="row g-3 ">
                <div class="col-md-6">
                    <label for="inputUsername4" class="form-label">账号*</label>
                    <input type="text" class="form-control" id="username">
                </div>
                <div class="col-md-6">
                    <label for="inputname4" class="form-label">昵称*</label>
                    <input type="text" class="form-control" id="name">
                </div>
                <div class="col-12">
                    <label for="inputAddress" class="form-label">密码*</label>
                    <input type="password" class="form-control" id="inputAddress" placeholder="密码无要求">
                </div>
                <div class="col-12">
                    <label for="inputAddress2" class="form-label">确认密码*</label>
                    <input type="password" class="form-control" id="inputAddress2" placeholder="请确认密码一致">
                </div>
                <div class="col12">
                    <div class="mb-3">
                        <label for="exampleFormControlTextarea1" class="form-label">自我介绍</label>
                        <textarea class="form-control" id="infp" rows="4"  placeholder="可不填"></textarea>
                    </div>
                </div>
                <div class="col-12">
                    <button type="submit" class="btn btn-primary">注册</button>
                </div>
            </form>
        </div>
    </ContentField>
    
</template>

<script>
import ContentField from '@/components/ContentField.vue'
import { ref } from 'vue'
import axios from 'axios'
export default{
    components:{
            ContentField
        },
    setup(){
        let username = ref("")
        let name = ref("")
        let password = ref("")
        let password_confirm = ref("")
        let info = ref("")


        const register = () =>{
            axios.post("http://101.43.45.110:8000/api/settings/register/",{
                username:username.value,
                name:name.value,
                password:password.value,
                password_confirm : password_confirm.value,
                info : info.value,
            })
            .then(resp=>{
                console.log(success)
            })
            
            
        }
    }

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


</style>