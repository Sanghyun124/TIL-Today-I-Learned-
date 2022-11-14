<template>
  <div>
    <h1>로또</h1>
    <button @click="onClick">Get Luckey Numbers</button>
    <p>{{ numbers }}</p>
  </div>
</template>

<script src="https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.21/lodash.min.js"></script>
<script>
export default {
  name: "TheLotto",
  data() {
    return {
      numbers: "",
      lottos: _.range(1, 46),
    };
  },
  methods: {
    onClick: function () {
      console.log(this.lottos);
      this.numbers = _.sampleSize(this.lottos, 6);
    },
  },
};
</script>

<style>
</style>
