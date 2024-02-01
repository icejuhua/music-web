<template>
    <!-- Modal -->
<div class="modal fade" id="infomodel" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
  <div class="modal-dialog modal-xl">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="staticBackdropLabel">修改个人信息</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <form class="row g-3" @submit.prevent="changeinfo">
                <div class="col-md-6">
                    <label for="username" class="form-label">用户名*</label>
                    <input v-model="new_name" type="text" class="form-control" id="username">
                </div>
                <div class="col12">
                    <div class="mb-3">
                        <label for="info" class="form-label">自我介绍</label>
                        <textarea v-model="new_info" class="form-control" id="infp" rows="4"  placeholder="可不填"></textarea>
                    </div>
                </div>
                <button  type="submit" class="btn btn-primary">提交</button>
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
import { useStore } from 'vuex';
import { ref } from 'vue';
export default{
    setup(){
        let new_info = ref('')
        let new_name = ref('')
        const store = useStore()
        const changeinfo = () =>{
            console.log("123");
            store.dispatch("changeinfo",{
                name:new_name.value,
                info:new_info.value,
                success(){
                    
                },
                error(){
                    
                }
            })
            
        };
        return{
            changeinfo,
            new_info,
            new_name
        }

    }
}
</script>

<style scoped>

</style>