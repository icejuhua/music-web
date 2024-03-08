<template>
    <div v-if="flag" >
        <APlayer  :audio="audio" ref="aplayer"></APlayer>
        <div>
            <el-table stripe :data="audio" border style="width: 100%">
                <el-table-column prop="name" label="乐曲名" width="180" />
                <el-table-column prop="artist" label="作者" width="180" />
                <el-table-column prop="total_time" label="时长" />
                <el-table-column  label="操作">
                    <template #default="{ row }">
                        <el-button  @click="handleButtonClick(row)" type="primary">下载</el-button>
                        <el-dropdown @command="handleCommand">
                            <el-button class="tr-download-btn" type="info">
                                转码下载<el-icon class="el-icon--right"><arrow-down /></el-icon>
                            </el-button>
                            <template #dropdown>
                            <el-dropdown-menu>
                                <el-dropdown-item @click="download_music_encode(row,'mp3')" command="mp3">mp3</el-dropdown-item>
                                <el-dropdown-item @click="download_music_encode(row,'flac')" command="flac">flac</el-dropdown-item>
                                <el-dropdown-item @click="download_music_encode(row,'wav')" command="wav">wav</el-dropdown-item>
                            </el-dropdown-menu>
                            </template>
                        </el-dropdown>
                        <router-link :to="{name:'music_info'}">
                            <el-button @click="detailBtn(row)" class="detail">详情</el-button>
                        </router-link>
                        <div v-if="$route.name == 'main_page_view'">
                            <el-button v-if="!row.add_status" circle @click="addMusicButton(row)" type="primary" class="Plus">
                                <el-icon size="30"><CirclePlus /></el-icon>
                            </el-button>
                            <el-button v-else circle class="Close" type="primary"  @click="delMusicButton(row)">
                                <el-icon plain ><CloseBold /></el-icon>
                            </el-button>
                        </div>
                        
                    </template>
                </el-table-column>
                <el-table-column v-if="false" prop="url" label="新列" show-overflow-tooltip></el-table-column>
                <el-table-column v-if="false" prop="music_type" label="新列" show-overflow-tooltip></el-table-column>
                <el-table-column v-if="false" prop="music_id" label="新列" show-overflow-tooltip></el-table-column>
                <el-table-column v-if="false" prop="add_status" label="新列" show-overflow-tooltip></el-table-column>
            </el-table>
            
            <div class="example-pagination-block">
            <!-- <div class="example-demonstration">分页</div> -->
            <el-pagination
                background
                layout="prev, pager, next ,total,sizes"
                :current-page="currentPage"
                :page-sizes="[5, 20, 30, 40]"
                :page-size="pageSize"
                :total="total"
                @current-change="handleCurrentChange"
                @size-change="handleSizeChange"
            />
            </div>
        </div>
    </div>
    
    
</template>
  
<script>

import APlayer from "@worstone/vue-aplayer";
import { useStore } from 'vuex'
import { ref  } from "vue"
import { useRoute } from "vue-router";
import axios from "axios";
import { ElNotification } from 'element-plus'
import { ElMessage } from 'element-plus'

export default {
components:{
            APlayer
},
    setup()
    {
        let audio = ref([])
        const store = useStore()  
        let flag = ref(false)
        //分页所需要的数据
        let currentPage = ref(1);
        let pageSize = ref(5);
        let total = ref(0);
        const route = useRoute()
        
        const download_success = () => {
        ElNotification({
            title: 'Success',
            message: '操作成功',
            type: 'success',
        })
        }

        const success_msg = () => {
        ElNotification({
            title: 'Success',
            message: '操作成功',
            type: 'success',
        })
        }
        const error_msg = () => {
        ElNotification({
            title: 'Error',
            message: '操作失败，请检查网络',
            type: 'error',
        })
        }

        const detailBtn = (row) =>{
            store.state.music.music_id = row.music_id
        }


        const get_info = (type) =>{
            store.dispatch("updataAccessFromRefresh")
            store.dispatch("get_music_info",{
                get_type:type,
                success(){
                    flag.value = true
                    audio.value = store.state.music.musicList
                    //获取数据长度
                    total.value = store.state.music.musicList.length;
                    // 在组件加载时触发一次初始化
                    handleCurrentChange(currentPage.value);
                },
                error(){
                    error_msg()
                }
        })
        }
        //不同的页面显示不同的效果
        if(route.name == 'main_page_view'){
            get_info("all")
        }
        else if(route.name == 'favorite_music'){
            get_info("favorite")
        }
        

        const handleCurrentChange = (newPage) => {
            // 根据新的页码和每页显示数量计算起始索引和结束索引
            currentPage.value = newPage
            let startIndex = (newPage - 1) * pageSize.value;
            let endIndex = newPage * pageSize.value;

            // 提取相应的数据段
            audio.value = store.state.music.musicList.slice(startIndex, endIndex);
        }
        const handleSizeChange = (newSize) => {
            // 更新每页显示的数量并重新计算数据段
            pageSize.value = newSize;
            handleCurrentChange(currentPage.value);
        }
        //点击按钮事件
        const handleButtonClick = (row) => {
            
            //调用下载
            store.dispatch("download_music",{
                url:row.url,
                name:row.name,
                music_type:row.music_type
            })
            window.alert("正在下载请稍后")
        };

        //添加歌单函数
        const addMusicButton = (row) => {
            axios.post(store.state.url+"music-list/add-favorite-music/",{
                user_id:store.state.user.user_id,
                music_id:row.music_id,
            },{
                headers:{
                    Authorization: "Bearer " + store.state.user.access_token,
                },
            })
            .then(resp =>{
                if(resp.data.error_msg == "success"){
                    get_info("all")
                    success_msg()
                }
                else{
                    error_msg()
                }
                
                console.log(resp.data);
            })
            .catch(resp =>{
                console.log(resp.data);
                error_msg()
            })
        }
        //删除歌单函数
        const delMusicButton = (row) => {
            axios.post(store.state.url+"music-list/del-favorite-music/",{
                user_id:store.state.user.user_id,
                music_id:row.music_id,
            },{
                headers:{
                    Authorization: "Bearer " + store.state.user.access_token,
                }
            })
            .then(resp =>{
                if(resp.data.error_msg == 'success'){
                    get_info("all"),
                    success_msg()
                }
                else{
                    error_msg()
                }
            })
            .catch(resp => {
                error_msg()
                console.log(resp.data);
            })
        }

        //下拉菜单的操作
        const handleCommand = (command) => {
            ElMessage(`正在下载格式为： ${command} `)
            
        }
        //转码下载
        const download_music_encode = (row,type) => {
            console.log(row,type);
            //每次请求前更新一下access
            store.dispatch("updataAccessFromRefresh")
            store.dispatch("download_music_encode",{
                music_type:row.music_type,
                url:row.url,
                music_name:row.name,
                encode_type:type,
                success(){
                    download_success()
                },
                error(){
                    error_msg()
                }
            })

        }   

                
        return {
            handleCurrentChange,
            handleButtonClick,
            handleSizeChange,
            addMusicButton,
            success_msg,
            error_msg,
            delMusicButton,
            handleCommand,
            download_music_encode,
            detailBtn,
            currentPage,
            pageSize,
            total,
            audio,
            flag,
        }
    },


    

};
</script>


<style scoped>
.tr-download-btn{
    margin-left: 20px;
}
.Plus{
    float: right;
}
.Close{
    float: right;
}
.detail{
    float: right;
}

</style>



