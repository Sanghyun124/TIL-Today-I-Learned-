<template>
  <div class="m-3 p-3 content ">
    <h1>2. 사이즈를 고르세요.</h1>
    <div id="size" class="selected" >
    <SizeListItem 
        v-for="(size,index) in getSizeList" 
        :key='index'
        :size=size
        :class="{'isSelected' : size.selected}"
      />
    </div>
  </div>
</template>

<script>
import SizeListItem from '@/components/SizeListItem'

export default {
  name: 'SizeList',
  components:{
    SizeListItem,
  },
  methods: {
    onSelectMenu: function () {
      const divTag=document.querySelector('#size')
      const check=this.$store.getters.getMenuList.filter((menu)=>{
        return menu.selected
      })
      if (check.length){
        divTag.classList.selected.display='block'
      } else {
        divTag.classList.selected.display='none'
      }
    },
  },
  computed: {
    getSizeList: function () {
      return this.$store.getters.getSizeList
    },
    getOnSelect(){
      return this.$store.getters.getOnSelect
    }
  },
}
</script>

<style>
  .selected{
    display:block;
  }
  .isSelected{
  background-color:lightgreen;
  color:white;
}
</style>