<script setup>
import {ref, onMounted} from "vue";
import {useRoute} from "vue-router";

import {retrievePostApi} from "@/services";

const route = useRoute()
const postId = route.params.id
const post = ref(null)
onMounted(async () => {
  post.value = await retrievePostApi(postId)
  console.log(post.value)
})
</script>

<template>
  <div class="py-lg-5">
    <v-row justify="center" no-gutters>
      <v-col cols="11" md="6" sm="10">
        <p class="text-h4 mb-2 hover-transition">State of the Union 2024</p>
        <p class="mb-4">🖊️ John Leider • 📅 September 8th, 2024</p>
        <div>
          <v-btn variant="tonal" append-icon="mdi-square-edit-outline" :to="`/posts/compose/${postId}`">编辑</v-btn>
          <span class="mx-2"></span>

          <v-btn variant="tonal" append-icon="mdi-publish" color="success">发布</v-btn>
          <span class="mx-2"></span>
          <v-btn variant="tonal" append-icon="mdi-delete-alert-outline" color="error">删除</v-btn>
        </div>
        <v-divider class="mb-6 mt-3"></v-divider>
        <div>
          <h2 class="my-5">Introduction</h2>
          <p>
            It’s been a long road to get where we are today, and looking back, I can’t help but feel proud of how far
            Vuetify has come. From humble beginnings to now surpassing Vuetify 2’s usage, the journey has been anything
            but easy, but we’ve always had our community to lean on. Today, I want to take some time to reflect on our
            past, acknowledge our wins and challenges, and share where we’re headed.
          </p>

          <h2 class="my-5">Looking Back – The Journey So Far</h2>
          <p>First, I’d like to reflect on what we’ve been up to for the past year. Since November 2023, we’ve hit some
            incredible milestones. This includes the release of v-data-table, and over 10 other new and old components.
            Each of these components was designed with developer feedback in mind, making the framework more flexible
            and
            feature-complete. We’ve also made significant progress on our ecosystem tools, with Vuetify One, Vuetify
            Bin,
            Vuetify Playground, and Vuetify Snips all seeing major updates.</p>


          <h2 class="my-5">v3.4 (Blackguard)</h2>
          <p>in November 2023 brought 8 new components:</p>

          <p>v-bottom-sheet</p>
          <p>v-data-iterator</p>
          <p>v-data-table</p>
          <p>v-date-picker</p>
          <p>v-infinite-scroll</p>
          <p>v-otp-input</p>
          <p>v-skeleton-loader</p>
          <p>v-stepper</p>
          <h2 class="my-5">v3.5 (Polaris)</h2>
          <p>in January 2024 was a maintenance cycle for bug fixes and performance improvements. This release focused
            heavily on refining existing components, ensuring performance remained high across all devices.</p>

          <h2 class="my-5">v3.6 (Nebula)</h2>
          <p>in April 2024 brought 5 new components:</p>

          <p>v-fab</p>
          <p>v-empty-state</p>
          <p>v-sparkline</p>
          <p>v-speed-dial</p>
          <p>v-confirm-edit</p>
          <p>v3.7 (Odyssey)</p>
          <p>in August 2024 improved sub v-menu support and added new input validation options, making form handling
            more
            intuitive and robust.</p>
        </div>
      </v-col>
    </v-row>
  </div>

</template>

<style scoped lang="sass">

</style>
