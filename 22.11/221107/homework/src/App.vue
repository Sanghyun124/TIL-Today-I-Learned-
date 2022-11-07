// App.vue

<template>
  <div id="app">
    <p>Counter: {{ $store.state.counter }}</p>
    <p>Counter x2: {{ counterDouble }}</p>
    <p></p>
    <button @click="increase">increase +</button>
    <button @click="decrease">decrease -</button>
  </div>
</template>

<script>
export default {
  name: 'App', 
  // data: function() {
  //   return {
  //     counter: 0,
  //   }
  // },
  methods: {
    increase: function () {
      // this.counter += 1
      this.$store.dispatch('increase')
    },
    decrease: function () {
      // this.counter -= 1
      this.$store.dispatch('decrease')
    },
  },
  computed: {
    // counterDouble: function () {
    //   return this.counter * 2
    // },
    counterDouble(){
      return this.$store.getters.counterDouble
    }
  },
}
</script>

<style>
</style>