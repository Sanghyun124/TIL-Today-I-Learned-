<template>
  <div id="app">
    <h1>캐릭터 진화 단계 가이드</h1>
    <div>
      <button class="btn" @click="clickHome">Home</button>
      <button class="btn" @click="clickStart">Start</button>
    </div>
    <div class="container row m-auto">
      <ssafyHome v-if="isStarted===false"/>
      <div v-else-if="isStarted===true" class="d-flex shadow">
      <div class="col-3 m-auto">
        <img @click="clickLeft" class="arrow" src="./assets/left.png" alt="">
      </div>
      <div class="col-6">
        <noColor v-if="page===1"/>
        <ssafLing v-else-if="page===2"/>
        <ssafLeaf v-else-if="page===3"/>
        <ssaFlower v-else-if="page===4"/>
      </div>
      <div class="col-3 m-auto">
        <img @click="clickRight" class="arrow" src="./assets/right.png" alt="">
      </div>
      </div>
    </div>
  

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
      } else{
        this.page++
      }
    }
  }
}
</script>

<style>
#app {
  font-family: "Noto Sans KR",Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

  .main{
    width:200px;
    height:200px;
  }

  .arrow{
    width:50px;
    height:50px;
  }

  .shadow{
    height:600px;
  }

  .btn{
    border: 1px solid rgb(197, 152, 5);
    margin:10px;
  }

</style>
