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
let quill = null
const options = {
  debug: 'info',
  readOnly: true,
  modules: {
    syntax: {hljs},
    toolbar: null,
   },
  theme: 'snow'
};


onMounted(async () => {
  post.value = await retrievePostApi(postId)
  quill = new Quill('#postsEditor', options);
  quill.setContents(post.value.content)
})
</script>

<template>
  <div class="py-lg-5">
    <v-row justify="center" no-gutters>
      <v-col cols="11" md="6" sm="10">
        <p class="text-h4 mb-2 hover-transition">{{post.title}}</p>
        <p class="mb-4">🖊️ John Leider • 📅 {{post.created_at}}</p>
        <div v-if="authState">
          <v-btn variant="tonal" append-icon="mdi-square-edit-outline" :to="`/posts/compose/${postId}`">编辑</v-btn>
          <span class="mx-2"></span>

          <v-btn variant="tonal" append-icon="mdi-publish" color="success">发布</v-btn>
          <span class="mx-2"></span>
          <v-btn variant="tonal" append-icon="mdi-delete-alert-outline" color="error">删除</v-btn>
        </div>
        <v-divider class="mt-3"></v-divider>
       <div id="postsEditor">

        </div>
      </v-col>
    </v-row>
  </div>

</template>

<style scoped lang="sass">

</style>
