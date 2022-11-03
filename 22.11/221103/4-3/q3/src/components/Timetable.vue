<template>
  <div>
    <br />
    <h2 class="">예약 페이지</h2>
    <div>
      <br />
      <h3 class="">선생님 선택</h3>
      <br />
      <button
        class="teacher-btn"
        @click="selectTeacher"
        :class="{ selected: activeE }"
        :value="'Eric'"
      >
        Eric
      </button>
      <button
        class="teacher-btn"
        @click="selectTeacher"
        :class="{ selected: activeT }"
        :value="'Tony'"
      >
        Tony
      </button>
    </div>
    <hr class="m-3" />
    <div class="">
      <br>
      <h4>시간 선택</h4>
      <br>
      <button
        v-for="time in times"
        :key="time"
        @click="isSelected"
        class="time-btn"
        :value="time"
      >
        {{ time }}
      </button>
    </div>
    <button class="commit-btn m-3 selected" @click="createCommit">예약 확정</button>
  </div>
</template>

<script>

export default {
  name: 'timeTable',
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
      else if (event.target.value==='Tony'){
        this.activeT=true
        this.activeE=false
      }
    },
    isSelected:function(event){
      if (this.selected.length===5){
        if(this.selected.includes(event.target.value)){
          const index=this.selected.indexOf(event.target.value)
          this.selected.splice(index,1)
          event.target.classList.remove('selected')
          }
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
    createCommit(){
      if(this.selectedTeacher===""){
        alert('선생님을 선택해 주세요!')
      }
      else if(this.selected.length===0){
        alert('시간을 선택해 주세요!')
      }
      else{
      const selectedTimes=[...this.selected]
      this.$emit('create-commit',selectedTimes,this.selectedTeacher)}
    }
  }
}
</script>