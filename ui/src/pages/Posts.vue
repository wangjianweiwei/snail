<template>
  <div class="py-lg-5">
    <v-layout>
      <v-row justify="center" no-gutters>
        <v-col cols="2">
          <v-row class="position-fixed">
            <v-col cols="12">
              <v-list density="compact" rounded="lg" variant="flat" color="#696CFF">
                  <v-list-item
                    rounded
                    color="#696CFF"
                    class="mx-2 my-1"
                    value="首页"
                    subtitle="首页"
                    to="/posts/list"
                    prepend-icon="mdi-page-first"
                  >
                  </v-list-item>
                  <v-list-item
                    value="分类"
                    color="#696CFF"
                    class="mx-2 my-1"
                    rounded
                    subtitle="分类"
                    to="/posts/category"
                    prepend-icon="mdi-view-grid-plus-outline"
                  >
                  </v-list-item>
                  <v-list-item
                    value="标签"
                    color="#696CFF"
                    class="mx-2 my-1"
                    rounded
                    subtitle="标签"
                    to="/posts/tag"
                    prepend-icon="mdi-tag-outline"
                  >
                  </v-list-item>
                  <v-list-item
                    value="时间线"
                    color="#696CFF"
                    class="mx-2 my-1"
                    rounded
                    subtitle="时间线"
                    to="/posts/timeline"
                    prepend-icon="mdi-timeline-check-outline"
                  >
                  </v-list-item>
                </v-list>
            </v-col>
            <v-col cols="12">
              <v-sheet rounded="lg" elevation="12">
                <v-list density="compact" lines="one" rounded="lg">
                  <v-list-item
                    value="首页"
                    color=""
                    subtitle="首页"
                    prepend-icon="$vuetify"
                  >
                  </v-list-item>
                  <v-list-item
                    value="分类"
                    color=""
                    subtitle="分类"
                    prepend-icon="$vuetify"
                  >
                  </v-list-item>
                  <v-list-item
                    value="标签"
                    color=""
                    subtitle="标签"
                    prepend-icon="$vuetify"
                  >
                  </v-list-item>
                </v-list>
              </v-sheet>
            </v-col>
          </v-row>
        </v-col>
        <v-col cols="6">
          <v-sheet rounded="lg" class="px-2 pb-5" elevation="12">
            <v-slide-x-reverse-transition>
              <router-view></router-view>
            </v-slide-x-reverse-transition>
          </v-sheet>
        </v-col>
      </v-row>
    </v-layout>
  </div>

</template>

<script setup>


const category = [
  {text: 'All(53)', icon: 'mdi-clock'},
  {text: 'Real-Time(20)', icon: 'mdi-clock'},
  {text: 'Audience(8)', icon: 'mdi-account'},
  {text: 'Conversions(17)', icon: 'mdi-flag'},
]
const debug = (a) => {
  console.log(a)

}
</script>
