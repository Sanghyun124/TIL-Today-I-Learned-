<template>
  <div class="menu-list m-3 p-3 content">
    <h1>3. 옵션을 고르세요.</h1>
    <ul class="option-list">
      <OptionListItem
        v-for="option in optionList"
        :key='option.type'
        :option=option
      />
    </ul>
  </div>
</template>

<script>
import OptionListItem from '@/components/OptionListItem'

export default {
  name: 'OptionList',
  components: {
    OptionListItem
  },
  computed: {
    optionList: function () {
      return this.$store.getters.optionList
    },
  },
  methods: {
    increase: function () {
    },
    decrease: function () {
    },
  },
}
</script>

<style>
.main{
  background-color: lightgray;
  border-radius:7px;
}
</style>