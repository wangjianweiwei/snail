<script setup>

import {ref, onMounted, reactive, nextTick} from "vue";
import Viewer from "viewerjs";
import 'viewerjs/dist/viewer.css';
import {getPhotosApi, uploadPhotosApi} from "@/services";

const drawer = ref(false)
const TimelineDialog = ref(false)
const UploadDialog = ref(false)
const UploadLoading = ref(false)
const event = ref("")
const files = ref([])
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
const photos = reactive([])
let viewer = null

onMounted(async () => {
  await getPhotos()
})

async function getPhotos() {
  photos.push(...await getPhotosApi())
  await nextTick();
  initViewer()
}

function initViewer() {
  if (viewer) {
    viewer.destroy()
  }
  viewer = new Viewer(document.getElementById('gallery'), {
    inline: false,
    zIndex: 10000,
    container: document.getElementById("preview"),
    fullscreen: false,
    movable: false,
    url(image) {
      return image.src.replace('_thumbnail_', '_');
    },
  });

}

async function upload() {
  UploadLoading.value = true
  await uploadPhotosApi(event.value, files.value)
  UploadLoading.value = false
  UploadDialog.value = false
  await getPhotos()
}

</script>

<template>
  <v-navigation-drawer
    v-model="drawer"
    location="bottom"
    temporary
  >
    <v-list nav>
      <v-list-item prepend-icon="mdi-cloud-upload-outline"
                   title="上传"
                   value="home"
                   @click="UploadDialog = true">
      </v-list-item>
      <v-list-item prepend-icon="mdi-timeline-clock-outline"
                   title="时间线"
                   value="account"
                   @click="TimelineDialog = true">
      </v-list-item>
      <v-list-item prepend-icon="mdi-account-group-outline"
                   title="Users"
                   value="users">
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
  <div id="preview"></div>
  <div id="gallery">
    <div class="gallery-item" :key="n.id" v-for="n in photos">
      <img :src="n.thumbnail" alt="12">
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
    v-model="TimelineDialog"
    transition="dialog-bottom-transition"
    fullscreen
  >
    <v-card>
      <v-toolbar height="50">
        <v-btn
          icon="mdi-close"
          @click="TimelineDialog = false"
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

  <v-dialog
    v-model="UploadDialog"
    width="30%"
  >
    <v-card
      :loading="UploadLoading"
      prepend-icon="mdi-cloud-upload-outline"
      title="上传"
    >
      <template v-slot:text>
        <v-form @submit.prevent>
          <v-text-field
            class="my-4"
            prepend-icon="mdi-draw"
            variant="outlined"
            density="compact"
            v-model="event"
            label="输入本次照片的主题">
          </v-text-field>
          <v-file-input
            class="my-4"
            multiple
            counter
            show-size
            chips
            v-model="files"
            prepend-icon="mdi-image"
            variant="outlined"
            density="compact"
            accept="image/*"
            label="选择要上传的照片">
          </v-file-input>
        </v-form>
      </template>
      <template v-slot:actions>
        <v-btn
          class="ms-auto"
          text="上 传"
          variant="tonal"
          @click="upload"
        ></v-btn>
      </template>
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
