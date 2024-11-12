<script setup>


import Quill from "quill";
import hljs from 'highlight.js';
import {onMounted} from "vue";
import {useRoute} from "vue-router";

import {ImageUploader} from "@/plugins/quilljsModules";
import {composePostApi} from "@/services";

Quill.register('modules/imageUploader', ImageUploader);

const route = useRoute()
const postId = route.params.id
const options = {
  debug: 'info',
  modules: {
    syntax: {hljs},
    toolbar: '#toolbar',
    // 工具栏配置
    imageUploader: {
      uploadUrl: 'http://127.0.0.1:8000/api/days-matter/image/upload' // 这里是你的后端图片上传接口
    }
  },
  theme: 'snow'
};
let quill = null

onMounted(() => {
  quill = new Quill('#postsEditor', options);
  window.quill = quill
})

async function save() {
  let content = quill.getContents()
  await composePostApi(postId, content)
}

</script>

<template>

  <div style="height: 100%">
    <v-row justify="center" no-gutters style="height: 100%">
      <v-col cols="11" md="6" sm="10" style="height: 100%">
        <v-row no-gutters style="height: 45px" class="d-flex justify-center align-center pa-1">
          <div id="toolbar">

            <select class="ql-size">
              <option value="small"></option>
              <option selected></option>
              <option value="large"></option>
              <option value="huge"></option>
            </select>
            <select class="ql-color"></select>
            <select class="ql-background"></select>
            <button class="ql-bold"></button>
            <button class="ql-italic"></button>
            <button class="ql-underline"></button>
            <button class="ql-strike"></button>
            <button class="ql-blockquote"></button>
            <button class="ql-list" value="ordered"></button>
            <button class="ql-list" value="bullet"></button>
            <select class="ql-align">
              <option selected></option>
              <option value="center"></option>
              <option value="right"></option>
              <option value="justify"></option>
            </select>
            <button class="ql-code-block" value="code"></button>
            <button class="ql-link"></button>
            <button class="ql-image"></button>
            <button @click="save">
              <svg class="ql-stroke" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><title>
                content-save-edit-outline</title>
                <path
                  d="M4 19H10V21H4C2.89 21 2 20.1 2 19V5C2 3.9 2.89 3 4 3H16L20 7V9.12L18 11.12V7.83L15.17 5H4V19M14 10V6H5V10H14M20.42 12.3C20.31 12.19 20.18 12.13 20.04 12.13C19.9 12.13 19.76 12.19 19.65 12.3L18.65 13.3L20.7 15.35L21.7 14.35C21.92 14.14 21.92 13.79 21.7 13.58L20.42 12.3M12 19.94V22H14.06L20.12 15.93L18.07 13.88L12 19.94M14 15C14 13.34 12.66 12 11 12S8 13.34 8 15 9.34 18 11 18C11.04 18 11.08 18 11.13 18L14 15.13C14 15.09 14 15.05 14 15"/>
              </svg>
            </button>
          </div>
        </v-row>
        <v-divider></v-divider>
        <v-row no-gutters style="height: calc(100% - 47px);overflow-y: scroll">
          <div id="postsEditor" style="height: 100%;width: 100%"></div>
        </v-row>
      </v-col>
    </v-row>
  </div>


</template>

<style scoped>
</style>
