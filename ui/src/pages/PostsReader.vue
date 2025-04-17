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
    layout: "adapt",
    darkMode: true,
    toc: {
      enable: true
    },
  });
  // 设置内容
  viewer.setDocument('json', post.value.content);


})
</script>

<template>
  <div class="py-lg-5">
    <v-row justify="center" no-gutters>
      <v-col cols="11" md="6">
        <p class="text-h4 mb-2 hover-transition">{{ post.title }}</p>
        <p class="mb-4">📅 {{ post.created_at }}</p>
        <div v-if="authState">
          <v-btn variant="tonal" append-icon="mdi-square-edit-outline" :to="`/posts/editor/${postId}`">编辑</v-btn>
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

<style>
.ne-doc-major-viewer .ne-viewer-layout-mode-adapt {
  padding: 10px 0 !important;
}
.ne-viewer-toc-sidebar {
  background: rgba(var(--v-theme-background)) !important;
}
</style>
