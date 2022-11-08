<template>
  <div class = "text-start m-3">
    <br>
    <h4><strong>주문 내역</strong></h4>
    <br>
    <h6>총 {{totalOrderCount}}건 : {{totalOrderPrice}}원</h6>
    <div>
      <OrderListItem
        v-for="(order,index) in orderList"
        :key=index
        :order=order
      />
    </div>
    <hr>
    <br>
  </div>
</template>

<script>
import OrderListItem from '@/components/OrderListItem'

export default {
  name: 'OrderList',
  components:{
    OrderListItem
  },
  computed: {
    orderList: function () {
      return this.$store.getters.orderList
    },
    totalOrderCount: function () {
      return this.$store.getters.totalOrderCount
    },
    totalOrderPrice: function () {
      return this.$store.getters.totalOrderPrice
    },
  },

}
</script>

<style scoped>

</style>