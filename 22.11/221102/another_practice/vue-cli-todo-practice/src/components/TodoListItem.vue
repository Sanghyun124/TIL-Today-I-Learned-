<template>
  <li>
    {{ todo.title }}
    <button @click="deleteTodo">x</button>
  </li>
</template>

<script>
export default {
  name: "TodoListItem",
  props: {
    todo: Object,
  },
  methods:{
    deleteTodo: function(){
      this.$emit('delete-todo',this.todo)
    }
  }
};
</script>

<style>
</style>