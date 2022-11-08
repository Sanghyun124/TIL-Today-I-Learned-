<template>
  <div class = 'd-flex text-start m-2 p-1'>
    <span class="me-auto">{{option.type}}</span>
    <button @click="decrease">-</button>
    <span class="">{{option.count}}</span>
    <button @click="increase">+</button>
  </div>
</template>

<script>
export default {
  name: 'OptionListItem',
  props: {
    option: Object,
  },
  methods: {
    increase() {
      this.$store.dispatch('increase',this.option)
    },
    decrease() {
      this.$store.dispatch('decrease',this.option)
    },
  },
}
</script>

<style scoped>
div{
    border:1px solid black;
    border-radius:7px;
  }
button{
  width:25px;
  height:25px;
  border-radius:100%;
}
</style>