<template>
  <div class="about">
    <h1>This is an about page</h1>
    <router-link :to="{name:'home'}">Home</router-link>|
    <button @click="toHome">홈으로</button>
    <input type="text" @keyup.enter="inputUserName" v-model="userName">
  </div>
</template>

<script>

export default {
  name: "AboutView",
  data(){
    return{
      userName:'',
    }
  },
  methods: {
    toHome() {
      this.$router.push({ name: "home" });
    },
    inputUserName(){
      this.$router.push({name:"hello" , params:{userName:this.userName}})
    }
  },
};
</script>
