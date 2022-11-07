<template>
  <div id="app">
    <input type="text" @keyup.enter="addToList" v-model="message">
    <p v-for="msg in msg_list" :key="msg">{{msg}}</p>
  </div>
</template>

<script>

export default {
  name: 'App',
  components: {
  },
  data(){
    return{
      message:null,
    }
  },
  computed:{
    msg_list(){
      return this.$store.state.msg_list
    }
  },
  methods:{
    addToList(){
      const msg=this.message
      this.$store.dispatch('pushMessage',msg)
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
