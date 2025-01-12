<template>
  <div class="py-lg-5">
    <v-row justify="center" no-gutters>
      <v-col cols="11" md="6" sm="11">
        <p class="text-h4 mb-2 mt-4 font-weight-black">博客</p>
        <p>Latest news, updates, and stories about Me.</p>
        <v-divider class="my-6"></v-divider>
        <div :key="post.id" v-for="post in posts">
          <p class="text-h5 mb-2 hover-transition">{{ post.title }}</p>
          <p class="mb-4">
            <span class="mr-1">📅 {{ post.created_at }}</span>

          </p>
          <p class="text-medium-emphasis font-weight-light">{{ post.abstract }}</p>
          <div class="text-end pt-4">
            <v-btn variant="text" append-icon="mdi-page-next-outline" :to="`/posts/preview/${post.id}`"
                   text="read more"></v-btn>
          </div>
          <v-divider class="my-6"></v-divider>
        </div>
        <div class="mt-8">
          <v-pagination @update:modelValue="changePage" :model-value="page" variant="text" active-color="primary"
                        size="x-large" :length="postCount"></v-pagination>
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

<script setup>
import {onMounted, ref} from "vue";
import {getPostsApi, createPostApi} from "@/services";
import {router} from "@/plugins/router";

const authState = localStorage.getItem("token")
console.log(authState)
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
  console.log(data)
  await router.push(`/posts/compose/${data["id"]}`)
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

<style>
.hover-transition {
  transition: color 0.5s ease;
}
</style>
