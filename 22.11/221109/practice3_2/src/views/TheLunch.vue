<template>
  <div>
    <h1>점심메뉴</h1>
    <button @click="onClickPick">Pick Lunch</button>
    <p>{{ menu }}</p>
    <br>
    <h1>로또를 뽑아보자</h1>
    <button @click="toLotto">Pick Lotto</button>
  </div>
</template>

<script src="https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.21/lodash.min.js"></script>
<script>
export default {
  name: "TheLunch",
  data() {
    return {
      menus: [
        "햄버거",
        "스파게티",
        "스테이크",
        "국밥",
        "피자",
        "치킨",
        "간장게장",
        "짬뽕",
        "짜장면",
        "볶음밥",
        "그라탕",
        "리조또",
        "불고기필라프",
      ],
      menu: "",
    };
  },
  methods: {
    onClickPick() {
      this.menu = this.menus[_.random(0, 12)];
    },
    toLotto(){
      this.$router.push({name:'TheLotto', params:{num:6}})
    }
  },
};
</script>

<style>
</style>