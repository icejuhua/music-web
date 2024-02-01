<template>
    <el-upload
      :data="{
        token:qiniuToken,
        key:'icejuhua.png'
      }"
      class="upload-demo"
      drag
      action="https://up-z2.qiniup.com"
      accept=".png"
      :limit=1
      multiple
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

export default{
    setup(){
        let qiniuToken = ref('')
        const store = useStore()
        
        store.dispatch("getupload_token",{
            success(resp){
                qiniuToken.value = resp.data.upload_token
                console.log("token success",qiniuToken.value);
            },
            error(resp){
                console.log(resp);
            }

        });
            
        return{
            qiniuToken
        }

    }
}
</script>
  