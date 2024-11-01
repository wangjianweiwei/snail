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
    // 工具栏配置
    toolbar: {
      container: [
        [{header: [1, 2, 3, 4, 5, 6, false]}],         // 标题
        ["bold", "italic", "underline", "strike"],       // 加粗 斜体 下划线 删除线
        ["blockquote", "code-block"],                    // 引用  代码块
        [{list: "ordered"}, {list: "bullet"}],       // 有序、无序列表
        [{indent: "-1"}, {indent: "+1"}],            // 缩进
        [{color: []}, {background: []}],             // 字体颜色、字体背景颜色
        [{align: []}],                                 // 对齐方式
        ["clean"],                                       // 清除文本格式
        ["link", "image"]                       // 链接、图片、视频
      ],
    },
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

  <div class="py-lg-5">
    <v-row justify="center" no-gutters>
      <v-col cols="11" md="6" sm="10">
        <div id="postsEditor"></div>
      </v-col>
    </v-row>
  </div>


</template>

<style scoped>
</style>
