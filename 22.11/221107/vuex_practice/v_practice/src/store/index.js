import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    msg_list:[],
  },
  getters: {
  },
  mutations: {
    PUSH_MESSAGE(state,msg){
      state.msg_list.push(msg)
    }
  },
  actions: {
    pushMessage(context,msg){
      context.commit('PUSH_MESSAGE',msg)
    }
  },
  modules: {
  }
})
