<template>
  <div>
    <span
      @click="updateTodoStatus"
      :class="{ 'is-completed': todo.isCompleted }"
    >
      {{ todo.title }}
    </span>
    <button @click="deleteTodo">Delete</button>
  </div>
</template>

<script>
export default {
  name: "TodoListItem",
  props: {
    todo: Object,
  },
  methods: {
    deleteTodo() {
      // console.log('delete');
      this.$store.dispatch("deleteTodo", this.todo);
      // this.$store.commit('DELETE_TODO', this.todo)
    },
    updateTodoStatus() {
      this.$store.dispatch("updateTodoStatus", this.todo);
    },
  },
};
</script>

<style>
.is-completed {
  text-decoration-line: line-through;
}
</style>