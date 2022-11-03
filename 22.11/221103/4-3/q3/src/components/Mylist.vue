<template>
  <div class="now">
    <br />
    <h2>상담 신청 현황</h2>
    <br />
    <div>
      <h3>상담 선생님</h3>
      <div>성함 : {{ teacherName }}</div>
    </div>
    <hr class="m-4" />
    <div>
      <br />
      <h3>예약 현황</h3>
      <h6 class="d-inline">시간들 :</h6>
      <h6 class="d-inline" v-for="select in timeData" :key="select">
        {{ select }}
      </h6>
    </div>
    <hr class="m-4" />
    <br />
    <img alt="ssafy-logo" src="@/assets/ssafy-logo.png" />
  </div>
</template>

<script>
export default {
  name: "myList",
  props:{
    timeData:Array,
    teacherName:String
  },
  data(){
    return{
      selectedTeacher:""
    }
  }
};
</script>

<style>
</style>