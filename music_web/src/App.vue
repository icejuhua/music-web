<template>
   <NavBar class="navbar"/>
    <router-view/>
</template>



<script>
//import $ from 'jquery'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap/dist/js/bootstrap"
import NavBar from "@/components/NavBar.vue"
import axios from 'axios'
export default{        
    setup(){
        console.log("sennding");
            axios.post("http://101.43.45.110:8000/vue_test/",{
            message: '通信测试',
            error_message:"success",
        })
        .then(resp =>{
            console.log(resp.data);
        })  
        .catch(error =>{
            console.log(error.data);
        });
        
    
        },
        components:{
            NavBar,
        }

    }


</script>


<style>
body{
    background:url("./assets/img/background.jpg");
    background-size: cover;
}
.navbar{
    margin-top: 5px;
}

</style>
