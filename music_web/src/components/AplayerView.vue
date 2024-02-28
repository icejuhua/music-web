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
                                <el-dropdown-item command="a">mp3</el-dropdown-item>
                                <el-dropdown-item command="b">flac</el-dropdown-item>
                                <el-dropdown-item command="c">WAV</el-dropdown-item>
                            </el-dropdown-menu>
                            </template>
                        </el-dropdown>
                        <el-icon size="40" class="Plus"><Plus /></el-icon>
                    </template>
                </el-table-column>
                <el-table-column v-if="false" prop="url" label="新列" show-overflow-tooltip></el-table-column>
                <el-table-column v-if="false" prop="music_type" label="新列" show-overflow-tooltip></el-table-column>
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
    
        
        store.dispatch("get_music_info",{
            success(){
                flag.value = true
                audio.value = store.state.music.musicList
                //获取数据长度
                total.value = store.state.music.musicList.length;
                console.log(store.state.music.musicList);
                // 在组件加载时触发一次初始化
                handleCurrentChange(currentPage.value);
                
            }
        })

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
            console.log(row.url);
            //调用下载
            store.dispatch("download_music",{
                url:row.url,
                name:row.name,
                music_type:row.music_type
            })
            window.alert("正在下载请稍后")
        };
                
        return {
            handleCurrentChange,
            handleButtonClick,
            handleSizeChange,
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

</style>



