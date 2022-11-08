<template>
  <div class="d-flex justify-content-between m-2 p-1 align-items-center" @click="selectSize">
    <span>{{size.name}}</span>
    <span>{{size.price}}원</span>
  </div>
</template>

<script>
export default {
  name: 'SizeListItem',
  props: {
    size: Object,
  },
  methods:{
    selectSize(){
      this.$store.dispatch('updateSizeList',this.size)
    }
  },
}
</script>

<style scoped>
  div{
    border:1px solid black;
    border-radius:7px;
    height:40px
  }
</style>