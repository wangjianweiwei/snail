<script setup>
import {onMounted, ref} from "vue";
import {useRoute} from "vue-router";
import {composePostApi, imageUpload, retrievePostApi} from "@/services";

const route = useRoute()
const snackbar = ref(false)
const postId = route.params.id
let editor = null


async function save() {
  let content = editor.getDocument()
  console.log(content)
  await composePostApi(postId, content)
  snackbar.value = true
}

function handleCtrlS(event) {
  if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === 's') {
    event.preventDefault(); // 阻止默认保存行为
    save()
    snackbar.value = true
  }
}

onMounted(async () => {
  console.log(postId)
  let data = await retrievePostApi(postId)
  const {createOpenEditor} = window.Doc;
  // 创建编辑器
  editor = createOpenEditor(document.getElementById('editor'), {
    darkMode: true,
    layout: "fixed",
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
          console.log(response)
          return {
            url: response.url,
            size: response.size, // 文件大小
            filename: response.filename
          }
        }
        console.log(response.data.data, "////")


      },
    },
  });
  // 设置内容
  editor.setDocument('json', data.content || {type: "element", name: "#root",});
  // 监听内容变动
  document.addEventListener('keydown', handleCtrlS, true);
})

</script>

<template>
  <div style="height: 100%">
    <div id="editor" style="height: 100%" class="ne-doc-major-editor"></div>
    <v-snackbar
      v-model="snackbar"
      timeout="2000"
      location="top right"
      variant="elevated"
      text="正在进行保存....."
    >
    </v-snackbar>
  </div>
</template>

<style scoped>

</style>
