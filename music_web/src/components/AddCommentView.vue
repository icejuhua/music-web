<template>
    <div class="addCommnetView">
        <el-input type="textarea" v-model="commentText">12</el-input>
        <el-button 
        size="large" 
        round color="#87CEFF" 
        class="comment-btn"
        auto-insert-space
        @click="addCommnet"
        >
            发表评论
        </el-button>
    </div>
</template>


<script>
import axios from 'axios'
import { useStore } from 'vuex'
import { ElNotification } from 'element-plus'
import { ref } from 'vue'
export default{
    emits : ["get_comments_list"],
    setup(props,context){
        const store = useStore()
        const commentText = ref("")
        console.log(props);
        const message_box = (title,message,type) => {
        ElNotification({
            title: title,
            message: message,
            type: type,
        })
        }

        
        const addCommnet= () =>{
            
            axios.post(store.state.url+"music-list/add-comments-info/",{
                user_id:store.state.user.user_id,
                music_id:store.state.music.music_id,
                comments_text:commentText.value,
            },{
                headers:{
                    Authorization: "Bearer " + store.state.user.access_token,
                },
            })
            .then(resp =>{
                if(resp.data.code == 200){
                    message_box("提示","添加成功","success")
                    commentText.value = ""
                    context.emit("get_comments_list")
                }
                else{
                
                    message_box("提示","添加失败，请检查网络:",resp.data.error_msg,"warning")
                }
            })
            .catch(resp=>{
                message_box("提示","网络错误:"+resp.data.error_msg,"error")
            })
        }

        return{
            addCommnet,
            message_box,
            commentText
        }
    }
}



</script>


<style scoped>
.addCommnetView{
    margin-top: 20px;
}
.comment-btn{
    margin-top: 20px;
}
</style>