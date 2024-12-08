<script setup>

import {ref, onMounted} from "vue";
import Viewer from "viewerjs";
import 'viewerjs/dist/viewer.css';

const drawer = ref(false)
const dialog = ref(false)


const years = ref([
  {
    color: 'cyan',
    year: '1960',
  },
  {
    color: 'green',
    year: '1970',
  },
  {
    color: 'pink',
    year: '1980',
  },
  {
    color: 'amber',
    year: '1990',
  },
  {
    color: 'orange',
    year: '2000',
  },
  {
    color: 'orange',
    year: '2000',
  },
  {
    color: 'orange',
    year: '2000',
  },
  {
    color: 'orange',
    year: '2000',
  },
])

const images = ref(['https://fengyuanchen.github.io/viewerjs/images/tibet-2.jpg', '/src/assets/images/OMG_7801.jpg', '/src/assets/images/OMG_8207.jpg', '/src/assets/thumbnail/OMG_8494.jpeg', '/src/assets/thumbnail/OMG_8318.jpeg', '/src/assets/thumbnail/OMG_8126.jpeg', '/src/assets/thumbnail/OMG_8290.jpeg', '/src/assets/thumbnail/OMG_8083.jpeg', '/src/assets/thumbnail/OMG_8097.jpeg', '/src/assets/thumbnail/OMG_8136.jpeg', '/src/assets/thumbnail/OMG_8384.jpeg', '/src/assets/thumbnail/OMG_8151.jpeg', '/src/assets/thumbnail/OMG_8227.jpeg', '/src/assets/thumbnail/OMG_8345.jpeg', '/src/assets/thumbnail/OMG_8387.jpeg', '/src/assets/thumbnail/OMG_7671.jpeg', '/src/assets/thumbnail/OMG_8220.jpeg', '/src/assets/thumbnail/OMG_8624.jpeg', '/src/assets/thumbnail/OMG_8368.jpeg', '/src/assets/thumbnail/YY__4535.jpeg', '/src/assets/thumbnail/YY__4496.jpeg', '/src/assets/thumbnail/YY__4480.jpeg', '/src/assets/thumbnail/OMG_8009.jpeg', '/src/assets/thumbnail/OMG_7930.jpeg', '/src/assets/thumbnail/OMG_8207.jpeg', '/src/assets/thumbnail/OMG_8603.jpeg', '/src/assets/thumbnail/OMG_8429.jpeg', '/src/assets/thumbnail/OMG_7860.jpeg', '/src/assets/thumbnail/OMG_8012.jpeg', '/src/assets/thumbnail/OMG_8172.jpeg', '/src/assets/thumbnail/OMG_8416.jpeg', '/src/assets/thumbnail/OMG_7898.jpeg', '/src/assets/thumbnail/OMG_8407.jpeg', '/src/assets/thumbnail/OMG_8570.jpeg', '/src/assets/thumbnail/OMG_7736.jpeg', '/src/assets/thumbnail/OMG_7988.jpeg', '/src/assets/thumbnail/OMG_7801.jpeg', '/src/assets/thumbnail/OMG_8298.jpeg', '/src/assets/thumbnail/OMG_8662.jpeg', '/src/assets/thumbnail/OMG_7637.jpeg', '/src/assets/thumbnail/OMG_8673.jpeg', '/src/assets/thumbnail/OMG_8049.jpeg', '/src/assets/thumbnail/OMG_8261.jpeg', '/src/assets/thumbnail/OMG_8275.jpeg', '/src/assets/thumbnail/OMG_8063.jpeg', '/src/assets/thumbnail/YY__4548.jpeg', '/src/assets/thumbnail/OMG_7621.jpeg', '/src/assets/thumbnail/OMG_7806.jpeg'])

onMounted(() => {
  let preview = document.getElementById("preview")
  const viewer = new Viewer(document.getElementById('gallery'), {
    inline: false,
    zIndex: 10000,
    container: preview,
    fullscreen: false,
    movable: false
  });
})
</script>

<template>
  <v-navigation-drawer
    v-model="drawer"
    location="bottom"
    temporary
  >
    <v-list nav>
      <v-list-item prepend-icon="mdi-cloud-upload-outline" title="上传" value="home"></v-list-item>
      <v-list-item prepend-icon="mdi-timeline-clock-outline" title="时间线" value="account"
                   @click="dialog = true"></v-list-item>
      <v-list-item prepend-icon="mdi-account-group-outline" title="Users" value="users"></v-list-item>
    </v-list>
  </v-navigation-drawer>
  <div id="preview"></div>
  <div id="gallery">
    <div class="gallery-item" v-for="n in images">
      <img :src="n" alt="12">
    </div>
  </div>
  <v-fab
    icon="mdi-dots-grid"
    location="bottom right"
    size="60"
    app
    appear
    @click="drawer = true"
  ></v-fab>
  <v-dialog
    v-model="dialog"
    transition="dialog-bottom-transition"
    fullscreen
  >
    <v-card>
      <v-toolbar height="50">
        <v-btn
          icon="mdi-close"
          @click="dialog = false"
        ></v-btn>
      </v-toolbar>
      <div class="pa-12">
        <v-timeline align="start">
          <v-timeline-item
            v-for="(year, i) in years"
            :key="i"
            :dot-color="year.color"
            size="small"
          >
            <template v-slot:opposite>
              <div
                :class="`pt-1 headline font-weight-bold text-${year.color}`"
                v-text="year.year"
              ></div>
            </template>
            <div>
              <h2 :class="`mt-n1 headline font-weight-light mb-4 text-${year.color}`">
                Lorem ipsum
              </h2>
              <div>
                Lorem ipsum dolor sit amet, no nam oblique veritus. Commune scaevola imperdiet nec ut, sed euismod
                convenire principes at. Est et nobis iisque percipit, an vim zril disputando voluptatibus, vix an
                salutandi sententiae.
              </div>
            </div>
          </v-timeline-item>
        </v-timeline>
      </div>
    </v-card>
  </v-dialog>
</template>


<style scoped>
#gallery {
  flex: 1; /* 左侧区域 */
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
  gap: 3px;
  padding: 0;
  overflow-y: auto;
  grid-auto-rows: 150px;
}

.gallery-item {
  position: relative;
  overflow: hidden;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  height: 150px; /* 固定高度，确保图片统一高度 */
}

.gallery-item img {
  width: 100%;
  height: 100%;
  object-fit: cover; /* 裁剪图片，使其适应容器 */
  display: block;
  transition: transform 0.3s ease;
  cursor: pointer;
}

.gallery-item img:hover {
  transform: scale(1.15);
}

</style>
