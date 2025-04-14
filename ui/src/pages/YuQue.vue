<script setup>
import {onMounted} from "vue";
import {imageUpload} from "@/services";

onMounted(() => {
  const {createOpenEditor} = window.Doc;
  // 创建编辑器
  const editor = createOpenEditor(document.getElementById('root'), {
    darkMode: true,
    placeholder: {
      tip: '请输入文字',
      emptyParagraphTip: '输入 / 唤起更多',
    },
    toc: {
      enable: true
    },
    input: {},
    image: {
      isCaptureImageURL() {
        return false;
      },
      createUploadPromise: async (request) => {
        const {type, data} = request;

        if (type === 'url') {
          // 假设你有一个接口可以根据URL转存图片
          console.log("需要转存的图片URL:", data);
        } else if (type === 'file') {
          // 假设上传文件
          const formData = new FormData();
          formData.append("image", data);
          // 使用 axios 上传图片
          let response = await imageUpload(formData)
          return Promise.resolve({
            url: response.data.data.url,
            size: response.data.data.size, // 文件大小
            filename: response.data.data.filename
          })
        }
        console.log(response.data.data, "////")


      },
    },
  });
  // 设置内容
  editor.setDocument('text/lake', '');
  // 监听内容变动
  editor.on('contentchange', () => {
    console.log(editor.getDocument());
  });
})

</script>

<template>
  <div id="root" style="height: 100%" class="ne-doc-major-editor"></div>
</template>

<style scoped>

</style>
