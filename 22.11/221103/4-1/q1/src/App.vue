<template>
  <div id="app">
    <h1>버튼 박스 제작</h1>
    <div class="shadow">
      <h2>예약 페이지</h2>
      <h3>시간 선택</h3>
      <div class="button-box mb-3">
        <button v-for="time in times" :key="time" @click="isSelected" class="" :value="time">{{ time }}</button>
      </div>
      <hr>
      <div class="selected-box">
        <h3>선택 시간 :</h3>
        <h3 v-for="select in selected" :key="select">{{select}}</h3>
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
      "09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30",
      "14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30",
      "19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",
      ],
      selected:[],
    }
  },
  methods:{
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
    }
  }

}
</script>

<style>
#app {
  font-family:'Noto Sans KR';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.shadow{
  box-shadow: 2px 1px 5px 2px gray;
  width:400px;
  margin:auto;
}

button{
  border:0px;
  background-color: white;
  width:50px;
  margin:5px;
  color:#84898C
}

.selected{
  background-color: lightblue;
  color: darkblue;
}

.line {
  color:darkblue;
}

.selected-box{
  display:flex;
}

h3{
  margin:5px;
}

</style>
