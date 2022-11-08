<template>
  <li class="d-flex align-items-center">
      <img class="p-2" :src="order['menu'][0].image" alt="">
      <span class="p-2">{{order['menu'][0].title}} <br>
          사이즈:{{order['size'][0].name}}</span>
      <span class="ms-auto">가격:{{totalPrice}}<br>
      샷 {{order['option'][0].count}}회 | 
      헤이즐넛 시럽 {{order['option'][1].count}}회 | 
      바닐라 시럽 {{order['option'][2].count}}회 |</span>
  </li>
</template>

<script>
export default {
  name: 'OrderListItem',
  props: {
    order: Object,
  },
  computed: {
    totalPrice: function () {
      return this.order['menu'][0].price+this.order['size'][0].price+(this.order['option'][0].price*this.order['option'][0].count)+(this.order['option'][1].price*this.order['option'][1].count)+(this.order['option'][2].price*this.order['option'][2].count)
    },
  },
}
</script>

<style scoped>
li{
  list-style: none;
}
img{
  width:60px;
  height:60px;
  border-radius:7px;
}
</style>