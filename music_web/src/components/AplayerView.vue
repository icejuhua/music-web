<template>
    <div v-if="flag" >
        <APlayer  :audio="audio" ref="aplayer"></APlayer>

        <div>
            <el-table stripe :data="audio" border style="width: 100%">
                <el-table-column prop="name" label="乐曲名" width="180" />
                <el-table-column prop="artist" label="作者" width="180" />
                <el-table-column prop="total_time" label="时长" />
                <el-table-column  label="操作">
                    <el-button type="primary">编辑</el-button>
                    <el-button type="danger" >删除</el-button>
                </el-table-column>
            </el-table>
            <div class="example-pagination-block">
            <!-- <div class="example-demonstration">分页</div> -->
        
                <el-pagination
                    background
                    layout="prev, pager, next ,total,sizes"
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
    
        
        store.dispatch("get_music_info",{
            success(){
                flag.value = true
                audio.value = store.state.music.musicList
                
            }
        })
        return {
            audio,
            flag,
        }
    },


    

};
</script>


<style scoped>


</style>