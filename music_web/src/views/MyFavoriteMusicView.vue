<template>
    <div>
        <el-alert title="我的喜爱" type="success" effect="dark" :closable="false" center show-icon/>
        <ContentField>
            <AplayerView/>
        </ContentField>
        <el-button type="primary" @click="download_music">下载</el-button>
    </div>
</template>

<script>
import ContentField from '@/components/ContentField.vue'

import AplayerView from '@/components/AplayerView.vue';
import axios from 'axios';
import { useStore } from 'vuex';
export default{
    components:{
        ContentField,
        AplayerView
    },
    setup(){
        const store = useStore()

        const download_music = () =>{
            axios.post(store.state.url+"music-list/download-music/",{},{
                headers:{
                    Authorization: "Bearer " + store.state.user.access_token,
                }
            })
            .then(response=>{
                console.log(response);
                const blob = new Blob([response.data], { type: 'audio/mpeg' });
                const url = window.URL.createObjectURL(blob);
                const link = document.createElement('a');
                link.href = url;
                link.setAttribute('download', 'output.mp3');
                document.body.appendChild(link);
                link.click();
                document.body.removeChild(link);
            })
            .catch(resp=>{
                resp
            })

        }
        return{
            download_music
        }
    }
}



</script>

<style scoped>

</style>