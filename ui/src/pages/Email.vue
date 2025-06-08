<template>
  <div>
    <v-btn @click="onClick">click</v-btn>
    <v-snackbar-queue class="d-flex justify-center" v-model="messages"></v-snackbar-queue>
  </div>
</template>

<script setup>
import {ref} from 'vue'

const messages = ref([])


function onClick() {
  messages.value.push({
    text: "12312",
    timeout: 2000,
    variant: "flat",
    location: "top right"
  })
  console.log(messages.value)
}
</script>
