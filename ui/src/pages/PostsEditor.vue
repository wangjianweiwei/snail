<script setup>
import {onMounted, ref} from "vue";
import {useRoute} from "vue-router";
import {composePostApi, imageUpload, retrievePostApi} from "@/services";

const route = useRoute()
const snackbar = ref(false)
const snackbarText = ref("")
const postId = route.params.id
let editor = null


async function save() {
  let content = editor.getDocument()
  let res = await composePostApi(postId, content)
  snackbar.value = true
  if (res) {
    snackbarText.value = "保存成功"
  } else {
    snackbarText.value = "保存失败"
  }
}

function handleCtrlS(event) {
  if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === 's') {
    event.preventDefault(); // 阻止默认保存行为
    save()
  }
}

onMounted(async () => {
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
      color="grey-darken-3"
      timeout="700"
      location="top right"
      variant="elevated"
    >
      <template v-slot:text>
        <v-progress-circular
          color="primary"
          size="20"
          indeterminate
        ></v-progress-circular>
        <span class="ml-3">{{ snackbarText }}</span>
      </template>
    </v-snackbar>
  </div>
</template>

<style>
.lakex-dark-theme-dark {
  --lakex-editor-background-primary: rgba(var(--v-theme-background)) !important;
}
</style>
