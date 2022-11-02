<template>
  <div>
    <h1>App Child</h1>
    <input type="text" v-model="childData" @input="fromChild">
    <h3>App : {{appData}}</h3>
    <h3>Parent : {{parentData}}</h3>
    <h3>Child : {{childData}}</h3>
  </div>
</template>

<script>
export default {
    name:'AppChild',
    data(){
        return{
            childData:""
        }
    },
    props:{
        appData:String,
        parentData:String,
    },
    methods:{
        fromChild(){
            this.$emit('from-child', this.childData)
        }
    }

}
</script>

<style>

</style>