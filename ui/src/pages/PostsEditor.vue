<script setup>


import Quill from "quill";
import hljs from 'highlight.js';
import {onMounted} from "vue";
import {ImageUploader} from "@/plugins/quilljsModules";

Quill.register('modules/imageUploader', ImageUploader);


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


</script>

<template>
  <link href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/atom-one-dark.min.css" rel="stylesheet">

  <div style="height: 100%">
    <v-row justify="center" no-gutters style="height: 100%">
      <v-col cols="11" md="6" sm="10" style="height: 100%">
        <v-row no-gutters style="height: 45px" class="d-flex justify-center align-center pa-1">
          <div id="toolbar">
            <!-- Add font size dropdown -->
            <select class="ql-size" style="color: white">
              <option value="small"></option>
              <!-- Note a missing, thus falsy value, is used to reset to default -->
              <option selected></option>
              <option value="large"></option>
              <option value="huge"></option>
            </select>
            <!-- Add a bold button -->
            <button class="ql-bold" style="color: white"></button>
            <!-- Add subscript and superscript buttons -->
            <button class="ql-script" value="sub"></button>
            <button class="ql-script" value="super"></button>
          </div>
        </v-row>
        <v-row no-gutters style="height: calc(100% - 45px);overflow-y: scroll">
          <div id="postsEditor" style="height: 100%;width: 100%"></div>
        </v-row>
      </v-col>
    </v-row>
  </div>


</template>

<style scoped>
</style>
