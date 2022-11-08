<template>
  <div class="menu-list m-3 p-3 content">
    <h1 >1. 음료를 고르세요.</h1>
    <div>
      <MenuListItem 
        v-for="(menu,index) in getMenuList" 
        :key='index'
        :menu=menu
        :class="{'isSelected' : menu.selected}"
      />
    </div>
  </div>
</template>

<script>
import MenuListItem from '@/components/MenuListItem'

export default {
  name: 'MenuList',
  components: {
    MenuListItem
  },
  computed: {
    getMenuList: function () {
      return this.$store.getters.getMenuList
    },
  },
  methods: {
    onSelect(){
      this.$emit('onSelect')
    }
  //   selectMenu: function () {
  //     console.log(1);
  //     this.$store.dispatch('updateMenuList')
  //   },
  },
}
</script>

<style scoped>
.isSelected{
  background-color:lightgreen;
  color:white;
}

</style>