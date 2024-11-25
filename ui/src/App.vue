<script setup>
import {onMounted} from "vue";
import {checkInitializationApi} from "@/services";
import {router} from "@/plugins/router";

onMounted(async () => {
  let initialization = await checkInitializationApi()
  if (!initialization) {
    await router.push("/initialization")
  }
})

</script>


<template>
  <router-view></router-view>

</template>

<style>
.v-btn--icon:hover {
  transform: translateY(-2px);
  transition: transform 0.3s ease;
}
</style>
