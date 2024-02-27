<template>
    <el-upload
      :data="{
        token:qiniuToken,
        key:image_name,
      }"
      class="upload-demo"
      drag
      action="https://up-z2.qiniup.com"
      accept=".png"
      :limit=1
      multiple
     :on-success="refresh_CDN"
    >
      <el-icon class="el-icon--upload"><upload-filled /></el-icon>
      <div class="el-upload__text">
        Drop file here or <em>click to upload</em>
        
      </div>
      <template #tip>
        <div class="el-upload__tip">
          jpg/png files with a size less than 500kb
         
        </div>
      </template>
    </el-upload>
</template>

<script>
import { ref  } from 'vue';
import { useStore } from 'vuex';
import axios from 'axios';

export default{
    setup(){
        let qiniuToken = ref('')
        let image_name = ref('')
        const store = useStore()
        
        store.dispatch("getupload_token",{
            success(resp){
                qiniuToken.value = resp.data.upload_token
                image_name.value = resp.data.image_name
                console.log("token success",image_name.value);
            },
            error(resp){
                console.log(resp);
            }

        });

        const refresh_CDN = () => {
            console.log("刷新CDN");
            axios.post(
                "http://101.43.45.110:8000/api/settings/refresh-cdn/",{
                user_name: store.state.user.username
                },{
                headers: {
                    Authorization: "Bearer " + store.state.user.access_token
                }
            }
            )
                .then(resp => {
                console.log(resp.data.error_msg);

                })
                .catch(error => {
                console.error(error);
                });
            };
            
        return{
            qiniuToken,
            refresh_CDN,
            image_name
        }

    }
}
</script>
  