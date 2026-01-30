<script setup>
import {ref} from 'vue'

const open = ref(['Users'])

const admins = [
  ['Management', 'mdi-account-multiple-outline'],
  ['Settings', 'mdi-cog-outline'],
]
const cruds = [
  ['Create', 'mdi-plus-outline'],
  ['Read', 'mdi-file-outline'],
  ['Update', 'mdi-update'],
  ['Delete', 'mdi-delete'],
]
</script>

<template>
  <v-navigation-drawer>
    <v-list v-model:opened="open" nav density="compact" slim border="0">
      <v-list-group value="Admin">
        <template v-slot:activator="{ props }">
          <v-list-item
            v-bind="props"
            title="Admin"
          ></v-list-item>
        </template>


        <v-list-item
          v-for="([title, icon], i) in admins"
          :key="i"
          :title="title"
          :value="title"
          variant="text"
          rounded
          density="compact"
          slim
          nav
        ></v-list-item>
      </v-list-group>

      <v-list-group value="Actions">
        <template v-slot:activator="{ props }">
          <v-list-item
            v-bind="props"
            title="Actions"
          ></v-list-item>
        </template>

        <v-list-item
          v-for="([title, icon], i) in cruds"
          :key="i"
          :title="title"
          :value="title"
          variant="text"
          rounded
          density="compact"
          slim
          nav
        ></v-list-item>
      </v-list-group>
    </v-list>
  </v-navigation-drawer>
  <v-app-bar elevation="0">
    <v-breadcrumbs style="margin-bottom: 0" :items="['Foo', 'Bar', 'Fizz']"></v-breadcrumbs>
  </v-app-bar>
  <v-container>
    <p>asdasdasd</p>
    <p>asdasdasd</p>
    <p>asdasdasd</p>
    <p>asdasdasd</p>
    <p>asdasdasd</p>
    <p>asdasdasd</p>
    <p>asdasdasd</p>
    <p>asdasdasd</p>
    <p>asdasdasd</p>
    <p>asdasdasd</p>
    <p>asdasdasd</p>
    <p>asdasdasd</p>
    <p>asdasdasd</p>
    <p>asdasdasd</p>
    <p>asdasdasd</p>
    <p>asdasdasd</p>
    <p>asdasdasd</p>
    <p>asdasdasd</p>
    <p>asdasdasd</p>
    <p>asdasdasd</p>
    <p>asdasdasd</p>
    <p>asdasdasd</p>
    <p>asdasdasd</p>
    <p>asdasdasd</p>
    <p>asdasdasd</p>
    <p>asdasdasd</p>
    <p>asdasdasd</p>
    <p>asdasdasd</p>
    <p>asdasdasd</p>
    <p>asdasdasd</p>
    <p>asdasdasd</p>
    <p>asdasdasd</p>
    <p>asdasdasd</p>
    <p>asdasdasd</p>
    <p>asdasdasd</p>
    <p>asdasdasd</p>
    <p>asdasdasd</p>
    <p>asdasdasd</p>
    <p>asdasdasd</p>
    <p>asdasdasd</p>
    <p>asdasdasd</p>
    <p>asdasdasd</p>
    <p>asdasdasd</p>
    <p>asdasdasd</p>
    <p>asdasdasd</p>
  </v-container>


</template>

<style scoped>

</style>
