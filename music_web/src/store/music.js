
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
            
        },
        download_music(content,data){
            console.log("开始下载");
            console.log("data",data);
            console.log(data.url);
            
            axios.get(data.url, {
                responseType: 'blob'
            })
            .then(response => {
                const url = window.URL.createObjectURL(new Blob([response.data]));
                const link = document.createElement('a');
                link.href = url;
                link.setAttribute('download', data.name+data.music_type);
                document.body.appendChild(link);
                link.click();
            })
            .catch(error => {
                console.error('下载失败', error);
            });
        }


    },
    modules: {
        
    }
  })
  