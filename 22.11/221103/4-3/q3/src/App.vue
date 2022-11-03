<template>
  <div id="app">
    <h1>SSAFY 상담 예약 시스템</h1>
    <div class="container row shadow">
      <timeTable class="reservation" @create-commit="createCommit"/>
      <myList class="now" :time-data="timeData" :teacher-name="teacherName"/>
    </div>
  </div>
</template>

<script>
import myList from "@/components/Mylist"
import timeTable from "@/components/Timetable"

export default {
  name: 'App',
  components: {
    myList,
    timeTable,
  },
  data(){
    return{
      timeData:[],
      teacherName:"",
    }
  },
  methods:{
    createCommit:function(times,teacher){
      this.timeData=times
      this.teacherName=teacher
      console.log('commited',this.timeData,this.teacherName);
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
.shadow{
  box-shadow: 2px 1px 5px 2px gray;
  height:500px;
  width:900px;
  margin:auto;
  padding:0;
}

.now{
  background-color: lightsteelblue;
  width:450px;
}
.color{
  color: #0F4C81 #658dc63d #84898C #424242
  }

.reservation{
  width:450px;
}

.teacher-btn{
    border:1px solid darkblue;
  background-color: white;
  width:70px;
  height:40px;
  margin:5px;
  color:#84898C
}

.commit-btn{
    border:1px solid darkblue;
  background-color: white;
  width:100px;
  height:40px;
  margin:5px;
  color:#84898C
}

.time-btn{
    border:0px;
  background-color: white;
  width:50px;
  margin:5px;
  color:#84898C
}

hr{
  border:1px solid darkblue;
}

.selected{
  background-color: lightblue;
  color: darkblue;
}

h6{
  margin:5px;
}
</style>
