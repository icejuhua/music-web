<template>
    <div>
        <el-alert title="我的喜爱" type="success" effect="dark" :closable="false" center show-icon/>
        <ContentField>
            <AplayerView/>
        </ContentField>
    </div>
</template>

<script>
import ContentField from '@/components/ContentField.vue'

import AplayerView from '@/components/AplayerView.vue';
// import axios from 'axios';
// import { useStore } from 'vuex';
export default{
    components:{
        ContentField,
        AplayerView
    },
    setup(){
        //const store = useStore()

        
        return{
            
        }
    }
}



</script>

<style scoped>

</style>