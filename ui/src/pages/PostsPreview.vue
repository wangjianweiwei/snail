<script setup>
import {ref, onMounted} from "vue";
import {useRoute} from "vue-router";
import Quill from "quill";
import hljs from 'highlight.js';

import {retrievePostApi} from "@/services";

const authState = localStorage.getItem("token")
const route = useRoute()
const postId = route.params.id
const post = ref({})


onMounted(async () => {
  post.value = await retrievePostApi(postId)
  const {createOpenViewer} = window.Doc;
  // 创建阅读器
  const viewer = createOpenViewer(document.getElementById('editor'), {
    layout: "fixed",
    darkMode: true,
  });
  // 设置内容
  viewer.setDocument('json', post.value.content);


})
</script>

<template>
  <div class="py-lg-12">
    <v-row justify="center" no-gutters>
      <v-col cols="5">
        <p class="text-h4 mb-2 hover-transition">{{ post.title }}</p>
        <p class="mb-4">📅 {{ post.created_at }}</p>
        <div v-if="authState">
          <v-btn variant="tonal" append-icon="mdi-square-edit-outline" :to="`/posts/compose/${postId}`">编辑</v-btn>
          <span class="mx-2"></span>

          <v-btn variant="tonal" append-icon="mdi-publish" color="success">发布</v-btn>
          <span class="mx-2"></span>
          <v-btn variant="tonal" append-icon="mdi-delete-alert-outline" color="error">删除</v-btn>
        </div>
        <v-divider class="mt-3"></v-divider>
        <div id="editor" class="ne-doc-major-viewer"></div>
      </v-col>
    </v-row>
  </div>

</template>

<style scoped lang="sass">

</style>
