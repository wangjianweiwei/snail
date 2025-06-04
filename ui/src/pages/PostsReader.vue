<script setup>
import {ref, onMounted, watch} from "vue";
import {useTheme} from 'vuetify'
import {useRoute, useRouter} from "vue-router";
import {retrievePostApi, deletePostApi, publishPostApi} from "@/services";
import {useI18n} from "vue-i18n";

const {t} = useI18n()
const theme = useTheme()
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
    defaultFontsize: 15,
    darkMode: theme.global.name.value === "dark",
    toc: {
      enable: false
    },
  });
  // 设置内容
  viewer.setDocument('json', post.value.content);
  watch(() => theme.global.name.value, (newVal, oldVal) => {
    if (newVal === "dark") {
      viewer.theme.setActiveTheme("dark-mode")
    } else {
      viewer.theme.setActiveTheme("default")
    }
  })


})


async function deletePost() {
  let data = await deletePostApi(postId)
  if (data.status) {
    await router.push("/posts/list")
  } else {
    snackbarText.value = "刪除失败"
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
  <v-row justify="center" class="py-4" style="height: 100%;" no-gutters>
    <v-col cols="11" xs="11" sm="11" md="11" lg="8" xl="7" xxl="6" style="height: 100%">
      <v-row class="d-flex justify-space-between align-center mt-4" dense>
        <v-col cols="12">
          <span class="text-h4 font-weight-bold">{{ post.title }}</span>
        </v-col>
      </v-row>
      <v-row class="align-center" dense>
        <v-col cols="12" md="6">
          <span class="mr-4">📅 {{ post.created_at }}</span>
          <span>🖊️ {{ post.wordcount }} {{ t('blog.text.words') }}</span>
        </v-col>
        <v-col cols="12" md="6" class="mt-3 d-flex justify-sm-start justify-md-end">
          <div v-if="authState">
            <v-btn append-icon="mdi-square-edit-outline" :to="`/posts/editor/${postId}`">
              {{ t("blog.btn.edit") }}
            </v-btn>
            <span class="mx-2"></span>

            <v-btn v-if="post.published" append-icon="mdi-publish-off" color="warning"
                   @click="publishPost(false)">{{ t('blog.btn.unpublishing') }}
            </v-btn>
            <v-btn v-else append-icon="mdi-publish" color="success" @click="publishPost(true)">
              {{ t("blog.btn.publish") }}
            </v-btn>

            <span class="mx-2"></span>
            <v-btn append-icon="mdi-delete-alert-outline" color="error" @click="deletePost">
              {{ t("blog.btn.delete") }}
            </v-btn>
          </div>
        </v-col>
      </v-row>
      <v-divider class="mt-3"></v-divider>
      <div id="editor" class="ne-doc-major-viewer"></div>
    </v-col>
  </v-row>

  <v-snackbar
    v-model="snackbar"
    :color="snackbarColor"
    timeout="1200"
    location="top right"
    variant="elevated"
    :text="snackbarText"
  >
  </v-snackbar>


</template>

<style>
.ne-doc-major-viewer .ne-viewer-layout-mode-adapt {
  padding: 10px 0 !important;
}

.ne-viewer-toc-sidebar {
  background: rgba(var(--v-theme-background)) !important;
}
</style>
