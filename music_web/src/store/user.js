

export default ({
    state: {
        id:'',
        username:'',
        name:'',
        photo_path:'',
        token:'',
        role:'',
        is_login:false,
    },
    getters: {
    },
    //一般放更新用户信息的函数
    mutations: {
        updataUser(state,user){
            state.id = user.id;
            state.username = user.username;
            state.name = user.name;
            state.photo = user.photo;
            state.is_login = user.is_login;
            state.userlevel = user.userlevel;
        },
        logout(state){
            state.id = '';
            state.username = '';
            state.name = '';
            state.photo = '';
            state.is_login = false;
            state.role = '';
        }
    },
    //一般放和后端通信的函数
    actions: {
    },
    modules: {
     
    }
  })
  