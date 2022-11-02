<template>
  <div id="app">
    <h1>App</h1>
    <input type="text" v-model='appData'/>
    <h3>App : {{appData}}</h3>
    <h3>Parent : {{parentData}}</h3>
    <h3>Child : {{childData}}</h3>
    <AppParent :app-data="appData" @from-parent="fromParent" @from-child="fromChild"/>
  </div>
</template>

<script>
import AppParent from '@/components/AppParent/'


export default {
  name: 'App',
  components: {
    AppParent,
  },
  data:function(){
    return{
      appData:"",
      parentData:"",
      childData:"",
    }
  },
  methods:{
    fromParent(pData){
      this.parentData=pData
    },
    fromChild(cData){
      this.childData=cData
    },
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
