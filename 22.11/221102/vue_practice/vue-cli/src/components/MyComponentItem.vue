<template>
  <div>
    <h3>MyComponent의 하위 컴포넌트</h3>
    <p>{{ staticProps }}</p>
    <p>{{ dynamicProps }}</p>
    <button @click="childToParent">클릭!</button>
    <input type="text" v-model="childInputData" @keyup.enter='childInput'>
  </div>
</template>

<script>
export default {
  name: "MyComponentItem",
  props: {
    staticProps: String,
    dynamicProps:String,
  },

  data : function() {
    return {
      childInputData:null,
    }
  },

  methods:{
    childToParent:function(){
      this.$emit('give-me-ma-money','안녕')
    },
    childInput: function(){
      this.$emit('child-input', this.childInputData)
      this.childInputData=null
    }
  }
};
</script>

<style>
</style>