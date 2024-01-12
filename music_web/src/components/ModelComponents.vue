<template>
    <!-- Modal -->
    <div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1"
        aria-labelledby="staticBackdropLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="staticBackdropLabel">小提示</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    {{ error_info }}
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-primary" data-bs-dismiss="modal">确认</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { ref } from 'vue';
    export default{
        props:{
            error_msg:{
                type:String,
                required:true,
            },
        },
        setup(error_msg){
            let error_info = ref('')
            if(error_msg.value != "success"){
                console.log(error_msg)
                error_info.value = "注册中"
                
            }
            else{
                error_info.value = "注册中"
            }
            return{
                error_info,
            }
        }
    };
</script>