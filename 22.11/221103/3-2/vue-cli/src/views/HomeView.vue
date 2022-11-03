<template>
  <div class="home">
    <h1>점심메뉴</h1>
    <button @click="pickMenu">Pick Lunch</button>
    <p>{{ menu }}</p>

  </div>
</template>

<script src="https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.21/lodash.min.js"></script>
<script>
// @ is an alias to /src

export default {
  name: 'HomeView',
  components: {
  },
  data(){
    return{
      menus:['족발', '애호박찌개', '봉골레파스타', '울면', '라면'],
      menu:"",
    }
  },
  methods:{
    pickMenu(){
      this.menu=_.sample(this.menus)
    }
  }
}
</script>
