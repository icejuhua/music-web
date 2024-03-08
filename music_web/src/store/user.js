import axios from 'axios';

export default ({
    
    state: {
        user_id:'',
        username:'',
        name:'',
        photo_path:'',
        access_token:'',
        refresh_token:'',
        role:'',
        info:'',
        is_login:false,
        upload_token:"",
        pulling_info:true,//当刷新界面的时候如果用户登录过，保证不会把登录界面显示一下
    },
    getters: {
    },
    //一般放更新用户信息的函数
    mutations: {
        updataUploadToken(state,upload_token){
            state.upload_token = upload_token
        },
        updataPullinginfo(state,pulling){
            state.pulling_info = pulling
        },
        updataUser(state,user){
            state.user_id = user.user_id
            state.username = user.username;
            state.name = user.name;
            state.photo_path = user.photo_path;
            state.role = user.role;
            state.info = user.info
            state.is_login = user.is_login
        },
        logout(state){
            state.user_id = '',
            state.username = '';
            state.name = '';
            state.photo_path = '';
            state.is_login = false;
            state.role = '';
            state.info = '';

        },
        updataAccess(state,token){
            state.access_token = token
            
        },
        updataRefresh(state,token){
            state.refresh_token = token
        },
        updatainfo(state,data){
            state.name = data.name
            state.info = data.info
        }
        
    },
    //一般放和后端通信的函数
    actions: {

        getupload_token(content,data){
            axios.post("http://101.43.45.110:8000/api/settings/upload-token/",{
            key_name:content.state.username
        },{
            headers:{
                Authorization: "Bearer " + content.state.access_token,
            },
            }
        )
        .then(resp => {
            content.commit("updataUploadToken",resp.data.upload_token)
            data.success(resp)
            //qiniuToken.value = resp.data.token
        })
        .catch(resp =>{
            data.error(resp)
        });
        },
        
        updataAccessFromRefresh(content){
            let refresh_token = localStorage.getItem("refresh_token")
            axios.post("http://101.43.45.110:8000/api/settings/token/refresh/",{
                refresh:refresh_token
            })
            .then(resp => {
                content.commit("updataAccess",resp.data.access)
                localStorage.setItem("access_token",resp.data.access)
                console.log("更新access成功")
            })
            .catch(resp =>{
                
                console.log("更新access失败",resp)
            })
        },
        login(content,data){
            console.log("login"),
            axios.post("http://101.43.45.110:8000/api/settings/token/",{
              username:data.username,
              password:data.password,
            })
            .then(resp =>{
              content.commit("updataAccess",resp.data.access)
              content.commit("updataRefresh",resp.data.refresh)
              localStorage.setItem("access_token",resp.data.access);
              localStorage.setItem("refresh_token",resp.data.refresh);
              
              data.success(resp)
              
            })
            .catch(resp =>{
                data.error(resp)
            })
        },
        //获取用户信息，不做序列化了
        getinfo(content,data){
            //console.log("getinfo");
            content.dispatch("updataAccessFromRefresh")
            axios.get("http://101.43.45.110:8000/api/settings/getinfo/",{
                headers:{
                    Authorization: "Bearer " + content.state.access_token,
                },
            })
            .then(resp=>{
                
                if(resp.data.error_msg == "success"){
                    content.commit("updataUser",{
                        ...resp.data,
                        is_login:true,
                    }),
                    
                    data.success()
                }
                else{
                    data.error()
                }
            })
            .catch(resp =>{
                console.log(resp);
                data.error()
            })
        },
        //退出，清空两个token，并且刷新当前界面
        logout(content){
            localStorage.removeItem("access_token")
            localStorage.removeItem("refresh_token")
            content.commit("logout")
            // let token = localStorage.getItem("access_token")
            // console.log("123",token);
            location.reload()
            

        },
        //更新用户信息
        changeinfo(content,data){
            
            content.dispatch("updataAccessFromRefresh")
            axios.post("http://101.43.45.110:8000/api/settings/changeinfo/",{
                name:data.name,
                info:data.info,
            },{
                headers:{
                    Authorization: "Bearer " + content.state.access_token,
                },
            }
                
                
            )
            .then(resp=>{
                console.log(resp);
                if(resp.data.error_msg == "success"){
                    content.commit("updataUser",{
                        name:data.name,
                        info:data.info,
                    })
                    data.success()
                }
                data.error()
                
            })
            .catch(resp=>{
                
                data.error(resp)
            })
        }


    },
    modules: {
     
    }
  })
  