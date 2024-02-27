

import axios from "axios"

export default({
    state: {
        //音乐列表，到时候从后端取值
        musicList:[]
        
        

    },
    getters: {
    },
    mutations: {
        updataMusicList(state,list){
            state.musicList = list
            
        }

    },
    actions: {
        get_music_info({commit,rootState},data){
            axios.get(rootState.url+"mainview/get-music-info/",{
                headers:{
                    Authorization: "Bearer " + rootState.user.access_token,
                },
            }
            )
            .then(resp => {
                commit("updataMusicList",resp.data.music_list)
                data.success()

            })
            .catch(resp => {
                console.log(resp);
            })
            
        }
    },
    modules: {
        
    }
  })
  