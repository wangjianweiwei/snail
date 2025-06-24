<template>
  <div>
    <v-btn @click="notify">click</v-btn>
  </div>
</template>

<script setup>
import {getCurrentInstance} from 'vue'

const {proxy} = getCurrentInstance()

function notify() {

  proxy.$message({
    message: '操作成功',
    type: 'warning'
  })
}
</script>
