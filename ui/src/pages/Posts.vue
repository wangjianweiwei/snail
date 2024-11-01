<template>
  <div class="py-lg-5">
    <v-row justify="center" no-gutters>
      <v-col cols="11" md="6" sm="10">
        <p class="text-h3 mb-2 mt-4 font-weight-black">Programming Language</p>
        <p>Latest news, updates, and stories about Vuetify.</p>
        <v-divider class="my-6"></v-divider>
        <div :key="n" v-for="n in 10">
          <p class="text-h4 mb-2 hover-transition">State of the Union 2024</p>
          <p class="mb-4">🖊️ John Leider • 📅 September 8th, 2024</p>
          <p class="text-medium-emphasis font-weight-light">It’s been a long road to get where we are today, and
            looking back, I can’t help but feel proud of how far Vuetify has come. From humble beginnings to now
            surpassing Vuetify 2’s usage, the journey has been anything but easy, but we’ve always had our
            community
            to lean on. Today, I want to take some time to reflect on our past, acknowledge our wins and
            challenges,
            and share where we’re headed…</p>
          <div class="text-end pt-4">
            <v-btn variant="text" append-icon="mdi-page-next-outline" to="/dashboards/posts/preview/10">Read More</v-btn>
          </div>
          <v-divider class="my-6"></v-divider>
        </div>
        <div class="mt-8">
          <v-pagination variant="text" active-color="primary" size="x-large" :length="10"></v-pagination>
        </div>
      </v-col>
    </v-row>
  </div>

</template>

<script setup>

</script>

<style>
.hover-transition {
  transition: color 0.5s ease;
}
</style>
