<template>
  <div id="app" class="container text-center">
    <h1>Coffee Order App</h1>
    <div class="d-flex justify-content-between main row m-0">
        <div class='col-4'><MenuList/></div>
        <div class='col-4'><SizeList/></div>
        <div class='col-4'><OptionList/></div>
    </div>
    <button class='btn btn-success w-100 mt-3' @click="doneSelect">장바구니 담기</button>
    <div class = "mt-3 main col-12"><OrderList/></div>

  </div>
</template>

<script>
import MenuList from '@/components/MenuList'
import SizeList from '@/components/SizeList'
import OrderList from '@/components/OrderList'
import OptionList from '@/components/OptionList'
export default {
  name: 'App',
  components:{
    MenuList,
    SizeList,
    OrderList,
    OptionList
  },
  methods:{
    doneSelect(){
      this.$store.dispatch('doneSelect')
    },
    loadOrder(){
      this.$store.dispatch('loadOrder')
    }
  },
  created(){
    this.loadOrder()
  },
}
</script>

<style>
* {
  box-sizing: border-box;
  font-family: 'Noto Sans KR', sans-serif;
  padding: 0;
  margin: 0;
}

ul {
  list-style: none;
  padding-left:0px;
}
.main{
  background-color: lightgray;
  border-radius:7px;
}

.content{
  background-color:white;
  border-radius:7px;
}
</style>
