<template>
   <NavBar class="navbar"/>
    <router-view/>
</template>



<script>
//import $ from 'jquery'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap/dist/js/bootstrap"
import NavBar from "@/components/NavBar.vue"


export default ({
    
    components:{
        NavBar,
    },
});

    




    

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
