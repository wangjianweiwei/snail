<script setup>
let a = [
  "https://adminpro-vuetify-main.netlify.app/assets/user-5-TcGtWTp3.jpg",
  "https://adminpro-vuetify-main.netlify.app/assets/user-6-Bw2gSpv_.jpg",
  "https://adminpro-vuetify-main.netlify.app/assets/user-2-idGLMY7R.jpg",
  "https://adminpro-vuetify-main.netlify.app/assets/user-3-HJ3opN5n.jpg",
]
const getAvatar = () => {
  let index = Math.floor((Math.random() * a.length))

  return a[index]
}
</script>

<template>
  <v-layout class="rounded-lg mx-6">
    <v-navigation-drawer width="380">
      <v-sheet>
        <div class="d-flex gap-2 pa-6">
          <div>
            <v-avatar size="60">
              <v-img
                alt="John"
                src="https://adminpro-vuetify-main.netlify.app/assets/user-1-CznVQ9Sv.jpg"
              ></v-img>
            </v-avatar>
          </div>
          <div>
            <h5 class="text-subtitle-1 font-weight-medium">Mathew Anderson</h5>
            <h6 class="text-subtitle-2">Designer</h6>
          </div>
        </div>
      </v-sheet>
      <v-sheet>
        <div class="d-flex gap-2 align-center pa-6">
          <v-text-field
            :loading="loading"
            append-inner-icon="mdi-magnify"
            density="compact"
            variant="outlined"
            color="blue"
            placeholder="Search Contact"
            @click:append-inner="onClick"
          ></v-text-field>
        </div>

      </v-sheet>
      <v-sheet>
        <v-list class="pa-2" activatable nav lines="two">
          <div v-for="n in 5">
            <v-list-item
              style="margin-bottom: 0"
              color="blue"
              density="comfortable"
              :prepend-avatar="getAvatar()"
              subtitle="john@google.com"
              title="John Leider"
            >
              <template v-slot:append>
                <span class="v-list-item-subtitle">14 minutes</span>
              </template>
            </v-list-item>
            <v-divider></v-divider>
          </div>

        </v-list>
      </v-sheet>
    </v-navigation-drawer>

    <v-app-bar height="80">
      <template #title>
        <v-list-item
          color="blue"
          density="comfortable"
          :prepend-avatar="getAvatar()"
          subtitle="online"
          title="John Leider"
        >
          <template v-slot:append>
            <v-icon class="ga-3" icon="mdi-phone"></v-icon>
            <v-icon class="ga-3" icon="mdi-video"></v-icon>
          </template>
        </v-list-item>
      </template>

    </v-app-bar>

    <v-main>
     <div style="height: 40%">
        <p>Main Content</p>
      <p>Main Content</p>
      <p>Main Content</p>
      <p>Main Content</p>
      <p>Main Content</p>
      <p>Main Content</p>
      <p>Main Content</p>
      <p>Main Content</p>
      <p>Main Content</p>
      <p>Main Content</p>
      <p>Main Content</p>
      <p>Main Content</p>
      <p>Main Content</p>
      <p>Main Content</p>
      <p>Main Content</p>
      <p>Main Content</p>
      <p>Main Content</p>
      <p>Main Content</p>
      <p>Main Content</p>
      <p>Main Content</p>
      <p>Main Content</p>
      <p>Main Content</p>
      <p>Main Content</p>
      <p>Main Content</p>
      <p>Main Content</p>
      <p>Main Content</p>
      <p>Main Content</p>
      <p>Main Content</p>
      <p>Main Content</p>
      <p>Main Content</p>
      <p>Main Content</p>
      <p>Main Content</p>
      <p>Main Content</p>
      <p>Main Content</p>
      <p>Main Content</p>
      <p>Main Content</p>
      <p>Main Content</p>
      <p>Main Content</p>
      <p>Main Content</p>
      <p>Main Content</p>
      <p>Main Content</p>
      <p>Main Content</p>
      <p>Main Content</p>
     </div>
    </v-main>
  </v-layout>
</template>

<style scoped>
</style>
