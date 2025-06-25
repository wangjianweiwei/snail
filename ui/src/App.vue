<script setup>
import {onMounted} from "vue";
import {checkInitializationApi} from "@/services";
import {router} from "@/plugins/router";
import {themeConfig} from "@/plugins/vuetify/theme";

onMounted(async () => {
  let initialization = await checkInitializationApi()
  if (!initialization) {
    await router.push("/initialization")
  }
})

</script>


<template>
  <v-locale-provider :locale="themeConfig.language.value[0]">
    <router-view></router-view>
  </v-locale-provider>


</template>

<style>
.v-btn--icon:hover {
  transform: translateY(-2px);
  transition: transform 0.3s ease;
}
</style>
