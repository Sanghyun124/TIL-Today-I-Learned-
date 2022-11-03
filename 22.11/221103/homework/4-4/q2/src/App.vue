<template>
  <div id="app">
    <h1>캐릭터 진화 단계 가이드</h1>
    <div>
      <button @click="clickHome">Home</button>
      <button @click="clickStart">Start</button>
    </div>
    <ssafyHome v-if="isStarted===false"/>
    <noColor v-else-if="isStarted===true&page===1"/>
    <ssafLing v-else-if="isStarted===true&page===2"/>
    <ssafLeaf v-else-if="isStarted===true&page===3"/>
    <ssaFlower v-else-if="isStarted===true&page===4"/>
  

  </div>
</template>

<script>
import ssafyHome from '@/components/Home'
import ssafLeaf from './components/Ssafleaf.vue'
import ssafLing from './components/Ssafling.vue'
import noColor from './components/Nocolor.vue'
import ssaFlower from './components/Ssaflower.vue'

export default {
  name: 'App',
  components: {
    ssafyHome,
    ssafLeaf,
    ssafLing,
    noColor,
    ssaFlower,
  },
  data(){
    return{
      page:1,
      isStarted:false,
    }
  },
  methods:{
    clickHome(){
      this.isStarted=false
      this.page=1
    },
    clickStart(){
      this.isStarted=true
    },
    clickLeft(){
      if(this.page!=1){
        this.page--
      }
    },
    clickRight(){
      if(this.page===4){
        alert('Home으로 돌아갑니다!')
        this.page=1
        this.isStarted=false
      }
    }
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
