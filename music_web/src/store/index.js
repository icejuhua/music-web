import { createStore } from 'vuex'
import ModuleUser from './user'
import ModuleMusic from './music'
export default createStore({
  state: {
    url:"http://101.43.45.110:8000/api/"
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    user:ModuleUser,
    music:ModuleMusic
  }
})
