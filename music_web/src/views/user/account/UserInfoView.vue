<template>
    <div class="row conterin-info">
            <div class="col-3">
                <div class="card" style="margin-top : 20px;">
                    <div class="card-body" style="text-align: center;">
                        <img class="head_img img-fluid"  :src=$store.state.user.photo_path alt="">
                    </div>
                    <div class="justify-content-center d-flex">
                        <el-button round size="large"  @click="dialogVisible = true" type="success">修改头像</el-button>
                    </div>
                    <div >
                        <el-dialog
                            v-model="dialogVisible"
                            title="Tips"
                            width="30%"
                            :before-close="handleClose"
                        >
                            <ImgUpLoad/>
                            <template #footer/>
                            <span class="dialog-footer"/>
                            <el-button @click="dialogVisible = false">Cancel</el-button>
                            <el-button type="primary" @click="dialogVisible = false">
                                Confirm
                        </el-button>
                        </el-dialog>
                    </div>
                </div>
            </div>
            <div class="col-9" style="margin-top : 20px;">
                <div class="card">
                    <div class="card-header">
                        个人信息
                    </div>
                    <div class="card-body">
                        <div class="form-group">
                        <label for="inputName">用户名</label>
                            <p id="inputName">{{$store.state.user.name}}</p>
                        </div>
                            <div class="form-group">
                        <label for="inputEmail">会员等级</label>
                            <p id="inputEmail">{{$store.state.user.role}}</p>
                        </div>
                        <div class="form-floating">
                            <textarea class="form-control" disabled placeholder="Leave a comment here" id="floatingTextarea2" style="height: 100px"></textarea>
                            <label for="floatingTextarea2">{{$store.state.user.info}}</label>
                            
                        </div>
                        <div class="d-flex justify-content-between" style="margin-top: 20px;">
                            <div>
                                <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#infomodel" >修改个人信息</button>
                                <UserInfoView/>
                                <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#passwordmodel" style="margin-left: 10px;" >修改密码</button>
                                <UserChangeModel/>
                            </div>
                            <button class="btn btn-secondary">歌单</button>
                        </div>
                    </div>
                </div>
            </div>
    </div>
</template>

<script>
import { useStore } from 'vuex';
import UserInfoView from '@/components/UserInfoModel.vue'
import UserChangeModel from '@/components/UserChangeModel.vue'
import { ref } from 'vue';
import ImgUpLoad from '@/components/ImgUpLoad.vue';

export default{
    components:{
        UserInfoView,
        UserChangeModel,
        ImgUpLoad,
    },
    setup(){
        const store = useStore()
        const dialogVisible = ref(false)
        console.log(store.state.user.photo_path);
        return{
            dialogVisible,
        }

    },
    
}

</script>

<style scoped>
.conterin-info{
    margin-left: 20px;
    margin-right: 20px;

}
</style>