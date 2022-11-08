import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    orderList: [],
    menuList: [
      {
        title:'아메리카노',
        price:2000,
        selected:false,
        image:'https://source.unsplash.com/featured/?americano'
      },
      {
        title:'카페라떼',
        price:3000,
        selected:false,
        image:'https://source.unsplash.com/featured/?cafelatte'
      },
      {
        title:'녹차라떼',
        price:4000,
        selected:false,
        image:'https://source.unsplash.com/featured/?matchalatte'
      },
    ],
    sizeList: [
      {
        name:'small',
        price:0,
        selected:false,
      },
      {
        name:'medium',
        price:500,
        selected:false,
      },
      {
        name:'big',
        price:1000,
        selected:false,
      },
    ],
    optionList:[
      {
        type:'샷',
        price:200,
        count:0,
      },
      {
        type:'헤이즐넛 시럽',
        price:300,
        count:0,
      },
      {
        type:'바닐라 시럽',
        price:500,
        count:0,
      },
    ],
    newOption:[
      {
        type:'샷',
        price:500,
        count:0
      },
    ]
  },
  getters: {
    getMenuList(state){
      return state.menuList
    },
    getSizeList(state){
      return state.sizeList
    },
    orderList(state){
      return state.orderList
    },
    totalOrderCount(state) {
      return state.orderList.length
    },
    totalOrderPrice: function (state) {
      let total=0
      for(let i=0;i<state.orderList.length;i++){
        total=total+state.orderList[i]['menu'][0].price+state.orderList[i]['size'][0].price+(state.orderList[i]['option'][0].price*state.orderList[i]['option'][0].count)+(state.orderList[i]['option'][1].price*state.orderList[i]['option'][1].count)+(state.orderList[i]['option'][2].price*state.orderList[i]['option'][2].count)
      }
      return total
    },
    optionList(state){
      return state.optionList
    }
  },
  mutations: {
    addOrder: function (state) {
      const selectedMenu=state.menuList.filter((menu)=>{
        return menu.selected
      })
      const selectedSize=state.sizeList.filter((size)=>{
        return size.selected
      })
      const options=JSON.parse(JSON.stringify(state.optionList))
      const selected={
        menu:selectedMenu,
        size:selectedSize,
        option:options
      }
      state.orderList.push(selected)
      const jsonOrderList=JSON.stringify(state.orderList)
      localStorage.setItem('orderList',jsonOrderList)

      console.log(state.orderList);

      state.menuList.forEach((menu)=>{
        menu.selected=false
      })

      state.sizeList.forEach((size)=>{
        size.selected=false
      })

      state.optionList.forEach((option)=>{
        option.count=0
      })
    },
    updateMenuList: function (state,selectedMenu) {
      state.menuList.forEach((menu)=>{
        menu.selected=false
      })
      const index=state.menuList.indexOf(selectedMenu)
      state.menuList[index].selected= !state.menuList[index].selected
    },
    updateSizeList: function (state,selectedSize) {
      state.sizeList.forEach((size)=>{
        size.selected=false
      })
      const index=state.sizeList.indexOf(selectedSize)
      state.sizeList[index].selected= !state.sizeList[index].selected
    },
    onSelect(state){
      state.onselect=true
    },
    updateOptionList(state,newOption){
      for(let option of state.optionList){
        if (option['type']===newOption['type']){
          const index=state.optionList.indexOf(option)
          state.optionList[index]=newOption
        }
      }

    },
    loadOrder(state){
      if(localStorage.getItem('orderList')){
      const localStorageOrder = localStorage.getItem('orderList')
      const parsedOrder=JSON.parse(localStorageOrder)
      state.orderList=parsedOrder
    }
    }

  },
  actions: {
    // addOrder: function (state) {
      
    // },
    updateMenuList: function (context,selectedMenu) {
      context.commit('updateMenuList',selectedMenu)
    },
    updateSizeList: function (context,selectedSize) {
      context.commit('updateSizeList',selectedSize)
    },
    onSelect(context){
      context.commit('onSelect')
    },
    doneSelect(context){
      context.commit('addOrder')
    },
    increase(context,selectedOption){
      const index=context.state.optionList.indexOf(selectedOption)
      const newOption=context.state.optionList[index]
      newOption.count+=1
      context.commit('updateOptionList',newOption)
    },
    decrease(context,selectedOption){
      const index=context.state.optionList.indexOf(selectedOption)
      const newOption=context.state.optionList[index]
      if(newOption.count>0){newOption.count-=1}
      context.commit('updateOptionList',newOption)
    },
    loadOrder(context){
      context.commit('loadOrder')
    }
  },
  modules: {
  }
})