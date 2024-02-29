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

    
// 解决ERROR ResizeObserver loop completed with undelivered notifications.

//问题的

const debounce = (fn, delay) => {

let timer = null;

return function () {

  let context = this;

  let args = arguments;

  clearTimeout(timer);

  timer = setTimeout(function () {

    fn.apply(context, args);

  }, delay);

}

}

// 解决ERROR ResizeObserver loop completed with undelivered notifications.

//问题的

const _ResizeObserver = window.ResizeObserver;

window.ResizeObserver = class ResizeObserver extends _ResizeObserver {

constructor(callback) {

  callback = debounce(callback, 16);

  super(callback);

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
