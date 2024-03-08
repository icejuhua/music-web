<template>
    <div class="music-info">
        <el-row :gutter="20">
            <el-col :span="6">
                <el-card shadow="hover">
                    <template #header>
                        <div class="card-header">
                            <el-text size="large"  tag="b">
                                <span>{{ $store.state.music.music_name }}</span>
                            </el-text>
                        </div>
                    </template>
                    <div class="grid-content ep-bg-purple-light">
                        <el-image :src="$store.state.music.music_image_path">
                            <template #placeholder>
                                <div class="image-slot">Loading<span class="dot">...</span></div>
                            </template>
                        </el-image>
                    </div>
                    <addConment @get_comments_list="get_comments_list"/>
                </el-card>
            </el-col>
            <el-col :span="18" v-loading="loading"
            element-loading-text="加载中..."
            element-loading-background="rgba(122, 122, 122, 0.8)"
            >
                <el-card shadow="hover">
                    <div class="grid-content ep-bg-purple">
                        <el-descriptions
                            title="歌曲信息"
                            direction="vertical"
                            :column="4"
                            :size="32"
                            border
                        >
                            <el-descriptions-item>
                                <template #label>
                                    <div class="cell-item">
                                        <el-icon><Service /></el-icon>
                                    创作者
                                    </div>
                                </template>
                                {{$store.state.music.music_artist}}
                            </el-descriptions-item>
                            <el-descriptions-item>
                                <template #label>
                                    <div class="cell-item">
                                        <el-icon><Watch /></el-icon>
                                        歌曲时长
                                    </div>
                                </template>
                                {{$store.state.music.music_total_time}}
                            </el-descriptions-item>
                            <el-descriptions-item :span="2">
                                <template #label>
                                    <div class="cell-item">
                                        <el-icon><Watch /></el-icon>
                                        是否需要会员
                                    </div>
                                </template>
                                <div v-if="$store.state.music.music_level == 2">
                                    需要
                                </div>
                                <div v-else>
                                    不需要
                                </div>
                            </el-descriptions-item>
                            <el-descriptions-item span="4">
                                <template #label>
                                    <div class="cell-item">
                                        <el-icon><Watch /></el-icon>
                                        歌曲信息
                                    </div>
                                </template>
                                <el-collapse>
                                    <el-collapse-item title="点击查看具体信息" name="2">
                                        <div tag="b"> 
                                            {{ $store.state.music.music_info }}
                                        </div>
                                    </el-collapse-item> 
                                </el-collapse>
                            </el-descriptions-item>
                            <el-descriptions-item label="评论">
                               
                            </el-descriptions-item>
                        </el-descriptions>

                        <el-table stripe border :data="comments" style="width: 100%" :table-layout="fixed">
                            <el-table-column prop="user_name" label="用户" />
                            <el-table-column prop="comments_text" label="内容" width="250"/>
                            <el-table-column prop="create_time" label="发表时间"/>
                            <el-table-column  label="操作" width="100">
                                <template #default="{ row }">
                                <el-button v-if="row.is_own" 
                                type="danger" @click="del_comment(row)" :icon="CircleCloseFilled" plain>
                                    删除
                                </el-button>
                                <el-button v-else
                                plain disabled>
                                    无法操作
                                </el-button>
                            </template>
                            </el-table-column>
                            <el-table-column v-if="false" prop="comment_id" label="新列" show-overflow-tooltip></el-table-column>
                            <el-table-column v-if="false" prop="is_own" label="新列" show-overflow-tooltip></el-table-column>
                        </el-table>
                    </div>
                </el-card>
            </el-col>
        </el-row>
        <el-backtop :right="100" :bottom="100" />
    </div>
</template>

<script>
import { useStore } from 'vuex'
import { ref } from 'vue'
import axios from 'axios'
import { ElNotification } from 'element-plus'
import addConment from '@/components/AddCommentView.vue'
export default{
    components:{
        addConment,
    },
    setup(){
        const loading  = ref(true)
        const store = useStore()
        let comments = ref([])

        const message_box = (title,error_msg,type) => {
            ElNotification({
                title: title,
                message: error_msg,
                type: type,
            })
        }
        //更新一下access_token
        store.dispatch("updataAccessFromRefresh")
        store.dispatch("get_detail_music_info",{
            music_id:store.state.music.music_id,
            success(){
                loading.value = false
                get_comments_list()
            },
            error(msg){
                console.log(msg);
            }
        })
        
        const get_comments_list = () =>{
            
            axios.get(store.state.url+"music-list/get-comments-info/",{
                headers:{Authorization: "Bearer " + store.state.user.access_token,
                },
                params:{
                    music_id:store.state.music.music_id,
                    user_id:store.state.user.user_id,
                },
            })
            .then(resp=>{
                if(resp.data.code == 200){
                    comments.value = resp.data.comments
                }
                else{
                    message_box("code 500","获取评论出错，请检查网络"+resp.data.error_msg,"warning")
                }
            })
            .catch(resp=>{  
                message_box("code 500","通信错误"+resp.data.error_msg,"error")
            })
        }


        const del_comment = (row) =>{
            console.log(row);
            axios.post(store.state.url+"music-list/del-comments-info/",{
                comment_id:row.comment_id,
                user_id:store.state.user.user_id
            },{
                headers:{
                    Authorization: "Bearer " + store.state.user.access_token,
                }
            })
            .then(resp=>{
                if(resp.data.code == 200){
                    get_comments_list()
                    message_box("提示","删除成功","success")
                }
                else {
                    message_box("错误","删除失败:"+resp.data.error_msg,"warning")
                }
            })
            .catch(resp=>{
                message_box("网络故障","删除失败，请检查网络"+resp.data.error_msg,"error")
            })
        }

        return{
            loading,
            comments,
            message_box,
            get_comments_list,
            del_comment
        }
    }
}
</script>

<style scoped>
.music-info{
    margin-top: 30px;
    margin-left: 20px;
    margin-right: 20px;
}

</style>