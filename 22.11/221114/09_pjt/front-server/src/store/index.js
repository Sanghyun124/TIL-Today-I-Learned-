import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '@/router'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'


export default new Vuex.Store({
  plugins:[
    createPersistedState(),
  ],
  state: {
    articles: [],
    token:null,
  },
  getters: {
    isLogin(state){
      return state.token ? true:false
    }
  },
  mutations: {
    GET_ARTICLES(state,articles){
      state.articles=articles
    },
    SAVE_TOKEN(state,token){
      state.token=token
      router.push({name:'ArticleView'})
    }
  },
  actions: {
    getArticles(context){
      axios({
        method:'get',
        url:`${API_URL}/api/v1/articles/`,
        headers:{
          Authorization:`Token ${context.state.token}`
        }
      })
        .then(res =>
          // console.log(res,context)
            context.commit("GET_ARTICLES",res.data)
          )
        .catch(err => console.log(err))
    },
    signUp(context, payload){
      const username=payload.username
      const password1=payload.password1
      const password2=payload.password2
      axios({
        method:'post',
        url:`${API_URL}/accounts/signup/`,
        data:{
          username,password1,password2
        }
      })
        .then((res)=>{
          console.log(1);
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch(err =>{console.log(err)})
    },
    logIn(context,payload){
      axios({
        method:'post',
        url:`${API_URL}/accounts/login/`,
        data:{
          username:payload.username,
          password:payload.password
        }
      })
      .then(res => {
        console.log(res.data.key);
        context.commit("SAVE_TOKEN", res.data.key)

      })
    }
  },
  modules: {
  }
})
