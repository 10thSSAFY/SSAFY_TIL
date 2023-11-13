<template>
  <div>
    <h1>Todo PJT</h1>
    <h2>완료된 Todo : {{ store.doneTodosCount }}</h2>
    <TodoForm />
    <TodoList />
  </div>
</template>

<script setup>
import TodoList from '@/components/TodoList.vue'
import TodoForm from '@/components/TodoForm.vue'

import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
</script>

<style scoped>
</style>
