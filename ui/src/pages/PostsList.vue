<script setup>
import {onMounted, ref} from "vue";
import { useI18n } from 'vue-i18n'
import {getPostsApi, createPostApi} from "@/services";
import {router} from "@/plugins/router";

const { t } = useI18n()
const authState = localStorage.getItem("token")
const posts = ref([])
const postCount = ref(0)
const page = ref(1)
const pageSize = ref(10)

/*获取列表页*/
async function getPosts() {
  let data = await getPostsApi(page.value, pageSize.value)
  posts.value = data['paged']
  postCount.value = data['page_count']
}

/*创建新的博客*/
async function createPost() {
  let data = await createPostApi("心情文章")
  await router.push(`/posts/editor/${data["id"]}`)
  // await getPosts()
}

/*切换页码*/
async function changePage(value) {
  page.value = value
  await getPosts()
}

onMounted(async () => {
  await getPosts()
})

</script>

<template>
  <div class="py-lg-5">
    <v-row justify="center" no-gutters>
      <v-col cols="11" md="7" sm="11">
        <p class="text-h4 mb-2 mt-4 font-weight-bold">{{t("menu.title.blog")}}</p>
        <p>{{ t("blog.subtitle")}}</p>
        <v-divider class="my-6"></v-divider>
        <div :key="post.id" v-for="post in posts">
          <p class="text-h6 mb-2 font-weight-bold">{{ post.title }}
            <v-chip
              v-if="authState && !post.published"
              class="ma-2"
              size="small"
              color="warning"
              label
            >
              {{ t("blog.unpublished") }}
            </v-chip>
          </p>
          <p class="mb-4">
            <span class="mr-4">📅 {{ post.created_at }}</span>
            <span>🖊️ {{ post.wordcount }} {{t('blog.text.words')}}</span>
          </p>
          <p class="text-medium-emphasis text-body-2">{{ post.abstract }}</p>
          <div class="d-flex justify-space-between justify-center align-center pt-5">
            <v-btn variant="text" append-icon="mdi-page-next-outline" :to="`/posts/reader/${post.id}`"
                   :text="t('blog.read')"></v-btn>
            <span class="text-medium-emphasis">
              <span><span class="mdi mdi-eye-outline"></span> 1209</span>
              <span class="ml-4"><span class="mdi mdi-thumb-up-outline"></span> 80</span>
              <span class="ml-4"><span class="mdi mdi-comment-text-outline"></span> 12</span>
            </span>
          </div>
          <v-divider class="my-5"></v-divider>
        </div>
        <div class="mt-8">
          <v-pagination @update:modelValue="changePage" :model-value="page" variant="text" active-color="primary"
                        :length="postCount"></v-pagination>
        </div>
      </v-col>
      <v-fab
        v-if="authState"
        icon="mdi-plus"
        location="bottom right"
        size="50"
        app
        appear
        @click="createPost"
      ></v-fab>
    </v-row>
  </div>

</template>


<style>

</style>
