<template>
  <div id="app">
    <h1><strong>SSAFY 상담 예약 시스템</strong></h1>
    <div class="container row shadow">
      <div class="reservation">
        <br>
        <h2 class="">예약 페이지</h2>
        <div>
          <br>
          <h3 class="">선생님 선택</h3>
          <br>
          <button class="teacher-btn" @click="selectTeacher" :class="{selected:activeE}" :value="'Eric'">Eric</button>
          <button class="teacher-btn" @click="selectTeacher" :class="{selected:activeT}" :value="'Tony'">Tony</button>
        </div>
        <hr class="m-4">
        <div class="">
          <br>
          <h4>시간 선택</h4>
          <br>
          <button v-for="time in times" :key="time" @click="isSelected" class="time-btn" :value="time">{{time}}</button>
        </div>
      </div>
      <div class="now">
        <br>
        <h2>상담 신청 현황</h2>
        <br>
        <div>
          <h3>상담 선생님</h3>
          <div>성함 : {{selectedTeacher}}</div>
        </div>
        <hr class="m-4">
        <div>
          <br>
          <h3>예약 현황</h3>
          <h6 class="d-inline">시간들 :</h6>
          <h6 class="d-inline" v-for="select in selected" :key="select">{{ select }}</h6>
        </div>
        <hr class="m-4">
        <br>
        <img alt="ssafy-logo" src="./assets/ssafy-logo.png">
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'App',
  components: {
  },
  data(){
    return{
      times: [
        "09:00","09:30","10:00","10:30","11:00","11:30",
        "12:00","12:30","13:00","13:30","14:00","14:30",
        "15:00","15:30","16:00","16:30","17:00","17:30",
      ],
      teachers:[
        {
          name:"Eric",
          selected:false
        },
        {
          name:"Tony",
          selected:false
        },
      ],
      selectedTeacher:"",
      selected:[],
      activeE:false,
      activeT:false,
    }
  },
  methods:{
    selectTeacher(event){
      this.selectedTeacher=event.target.value
      if(event.target.value==='Eric'){
        this.activeE=true
        this.activeT=false
      }
      else{
        this.activeT=true
        this.activeE=false
      }
    },
    isSelected:function(event){
      if (this.selected.length===5){
        if(this.selected.includes(event.target.value)){
          const index=this.selected.indexOf(event.target.value)
          this.selected.splice(index,1)
          event.target.classList.remove('selected')}
          else{
            alert('5타임까지만 신청할 수 있습니다.')}
        }
        else{
          if(this.selected.includes(event.target.value)){
            const index=this.selected.indexOf(event.target.value)
          this.selected.splice(index,1)
          event.target.classList.remove('selected')
        }
        else{
          this.selected.push(event.target.value)
          event.target.classList.add('selected')
        }

        }
    },
  }
}
</script>

<style>
#app {
  font-family: 'Noto Sans KR',Avenir, Helvetica, Arial, sans-serif;
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
