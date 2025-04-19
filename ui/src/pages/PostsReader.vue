<script setup>
import {ref, onMounted} from "vue";
import {useRoute, useRouter} from "vue-router";
import {retrievePostApi, deletePostApi, publishPostApi} from "@/services";

const authState = localStorage.getItem("token")
const route = useRoute()
const router = useRouter()
const postId = route.params.id
const post = ref({})
const snackbar = ref(false)
const snackbarColor = ref("primary")
const snackbarText = ref("")


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


async function deletePost() {
  let data = await deletePostApi(postId)
  if (data.status) {
    await router.push("/posts/list")
  } else {
    snackbarText.value = "刪除失敗"
    snackbar.value = true
  }
}

async function publishPost(status) {
  let data = await publishPostApi(postId, status)
  if (data.status) {
    post.value.published = status
    snackbarText.value = "成功"
    snackbar.value = true
  } else {
    snackbarText.value = "失败"
    snackbar.value = true
  }
}
</script>

<template>
  <div class="py-lg-5">
    <v-row justify="center" no-gutters>
      <v-col cols="11" md="6">
        <div class="d-flex justify-space-between align-center">
          <div>
            <p class="text-h4 mb-2 font-weight-bold">{{ post.title }}</p>
            <span class="mr-4">📅 {{ post.created_at }}</span>
            <span>🖊️ {{post.wordcount}}字</span>
          </div>
          <div v-if="authState">
            <v-btn variant="tonal" append-icon="mdi-square-edit-outline" :to="`/posts/editor/${postId}`">编辑</v-btn>
            <span class="mx-2"></span>

            <v-btn v-if="post.published" variant="tonal" append-icon="mdi-publish-off" color="warning" @click="publishPost(false)">取消发布</v-btn>
            <v-btn v-else variant="tonal" append-icon="mdi-publish" color="success" @click="publishPost(true)">发布</v-btn>

            <span class="mx-2"></span>
            <v-btn variant="tonal" append-icon="mdi-delete-alert-outline" color="error" @click="deletePost">删除</v-btn>
          </div>
        </div>

        <v-divider class="mt-3"></v-divider>
        <div id="editor" class="ne-doc-major-viewer"></div>
      </v-col>
      <v-snackbar
        v-model="snackbar"
        :color="snackbarColor"
        timeout="1200"
        location="top right"
        variant="elevated"
        :text="snackbarText"
      >
      </v-snackbar>
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
