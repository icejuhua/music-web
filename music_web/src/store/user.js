import axios from 'axios';

export default ({
    state: {
        username:'',
        name:'',
        photo_path:'',
        access_token:'',
        refresh_token:'',
        role:'',
        info:'',
        is_login:false,
        pulling_info:true,//当刷新界面的时候如果用户登录过，保证不会把登录界面显示一下
    },
    getters: {
    },
    //一般放更新用户信息的函数
    mutations: {
        updataPullinginfo(state,pulling){
            state.pulling_info = pulling
        },
        updataUser(state,user){
            state.username = user.username;
            state.name = user.name;
            state.photo_path = user.photo_path;
            state.role = user.role;
            state.info = user.info
            state.is_login = user.is_login
        },
        logout(state){
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
            
        }
    },
    //一般放和后端通信的函数
    actions: {
        login(content,data){
            console.log("sending login info"),
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
                    data.error(resp)
                }
            })
            .catch(resp =>{
                data.error(resp)
            })
        }


    },
    modules: {
     
    }
  })
  