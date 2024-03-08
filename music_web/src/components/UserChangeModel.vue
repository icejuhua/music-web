<template>
        <!-- Modal -->
<div class="modal fade" id="passwordmodel" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
  <div class="modal-dialog modal-xl">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="staticBackdropLabel">修改密码</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <form class="row g-3 " @submit.prevent="change_password">
                <div class="col-md-12">
                    <label for="old-password" class="form-label">旧密码*</label>
                    <input v-model="old_password" type="password" class="form-control" id="old-password">
                </div>
                <div class="col-md-6">
                    <label for="new-password" class="form-label">新密码*</label>
                    <input v-model="new_password" type="password" class="form-control" id="new-password">
                </div>
                <div class="col-md-6">
                    <label for="new-password-confirm" class="form-label">确认密码*</label>
                    <input v-model="confirm_password" type="password" class="form-control" id="new-password-confirm">
                </div>
                <button type="submit" class="btn btn-primary">提交</button>
            </form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">关闭</button>
        
      </div>
    </div>
  </div>
</div>
</template>

<script>
import { useStore } from 'vuex'
import { ref } from 'vue'
import { ElNotification } from 'element-plus'
import axios from 'axios'
export default{
  setup(){
    const store = useStore()
    let old_password = ref("")
    let new_password = ref("")
    let confirm_password = ref("")
    const message_box = (title,message,type) => {
        ElNotification({
            title: title,
            message: message,
            type: type,
        })
        }



    const change_password = () =>{
      axios.post(store.state.url+"settings/change-password/",{
          old_password:old_password.value,
          new_password:new_password.value,
          confirm_password:confirm_password.value,
      },{
        headers:{
          Authorization: "Bearer " + store.state.user.access_token,
        }
      })
      .then(resp=>{
        if(resp.data.code == 200){
          message_box("提示","修改成功","success")
        }
        else{
          message_box("错误","信息有误:"+resp.data.error_msg,"warning")
        }
        
      })
      .catch(resp=>{
        message_box("网络错误","修改失败，请检查网络"+resp.data.error_msg,"error")
      })
    }
    return{
        old_password,
        new_password,
        confirm_password,
        change_password,
    }
  }
}

</script>

<style scoped>

</style>