<template>
  <div class="d-flex justify-content-between m-2 p-1 align-items-center" @click="selectMenu">
    <img :src='menu.image' alt="">
    <span>{{menu.title}}</span>
    <span>{{menu.price}}원</span>
  </div>
</template>

<script>
export default {
  name: 'MenuListItem',
  props: {
    menu: Object,
  },
  methods:{
    selectMenu(){
      this.$store.dispatch('updateMenuList',this.menu)
      this.$store.dispatch('onSelect')
    }
  }
}
</script>

<style scoped>
img{
  height:30px;
  width:30px;
  border-radius:7px;
}

div{
    border:1px solid black;
    border-radius:7px;
  }
</style>