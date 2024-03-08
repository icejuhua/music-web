
import axios from "axios"

export default({
    state: {
        //单个的音乐数据，在查看音乐信息的时候使用
        music_id:"",
        music_name:"",
        music_artist:"",
        music_image_path:"",
        music_total_time:"",
        music_info:"",
        music_level:"",
        // 评论
        music_comments:"",
        //音乐列表，到时候从后端取值
        musicList:[],
    },
    getters: {
    },
    mutations: {
        updataMusicList(state,list){
            state.musicList = list
            
        },
        updataMusicInfo(state,music){
            state.music_name = music.music_name,
            state.music_image_path = music.music_image_path,
            state.music_total_time = music.music_total_time,
            state.music_info = music.music_info,
            state.music_level = music.music_level
            state.music_artist = music.music_artist
        }

    },
    actions: {
        


        //获取单条音乐信息
        get_detail_music_info({commit,rootState},data){
            axios.get(rootState.url+"music-list/get-detail-music-info/",{
                headers:{Authorization: "Bearer " + rootState.user.access_token,
                },
                params:{
                    music_id:data.music_id
                }
            })
            .then(resp=>{
                if(resp.data.error_msg == "success"){
                    commit("updataMusicInfo",resp.data.music_data)
                    data.success()
                }
                else data.error(resp.data.error_msg)
            })
            .catch(resp=>{
                console.log(resp.data);
                data.error()
            })
        },



        get_music_info({commit,rootState},data){
            console.log(data.get_type);
            axios.get(rootState.url+"mainview/get-music-info/",{
                headers:{
                    Authorization: "Bearer " + rootState.user.access_token,
                },
                params: {
                    get_type: data.get_type
                }
            },
            )
            .then(resp => {
                commit("updataMusicList",resp.data.music_list)
                data.success()

            })
            .catch(resp => {
                console.log(resp);
                data.error()
            })
            
        },
        download_music(content,data){
            console.log("开始下载");
            
            
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
                document.body.removeChild(link)
            })
            .catch(error => {
                console.error('下载失败', error);
            });
        },
        download_music_encode({rootState},data){
            
            axios.post(rootState.url+"music-list/download-music/",{
                music_type:data.music_type,
                url:data.url,
                music_name:data.music_name,
                encode_type:data.encode_type
            },{
                headers:{
                    Authorization: "Bearer " + rootState.user.access_token,
                }
            })
            .then(response => {
                console.log("开始下载",data.music_name+'.'+data.encode_type);
                console.log(response);
                const blob = new Blob([response.data], { type: 'audio/mpeg' });
                const url = window.URL.createObjectURL(blob);
                const link = document.createElement('a');
                link.href = url;
                link.setAttribute('download', data.music_name+'.'+data.encode_type);
                document.body.appendChild(link);
                link.click();
                document.body.removeChild(link);
                data.success()
            })
            .catch(resp=>{
                console.log("下载失败",resp);
                data.error()
            })
        }


    },
    modules: {
        
    }
  })
  