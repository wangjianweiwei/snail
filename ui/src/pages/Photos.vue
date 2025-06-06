<script setup>

import {ref, onMounted, reactive, nextTick} from "vue";
import Viewer from "viewerjs";
import 'viewerjs/dist/viewer.css';
import {getPhotosApi, uploadPhotosApi, getEventsApi} from "@/services";

const drawer = ref(false)
const TimelineDialog = ref(false)
const UploadDialog = ref(false)
const UploadLoading = ref(false)
const event = ref("")
const files = ref([])
const events = ref([])
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

async function getEvents() {
  events.value = await getEventsApi()
}

async function openTimelineDialog() {
  await getEvents()
  TimelineDialog.value = true
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
    movable: true,
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
    <div id="preview"></div>
    <div id="gallery">
      <div class="gallery-item" :key="n.id" v-for="n in photos">
        <img :src="n.thumbnail" alt="12">
      </div>
    </div>

    <v-navigation-drawer
      v-model="drawer"
      location="right"
      temporary
    >
      <v-list nav>
        <v-list-subheader>操 作</v-list-subheader>
        <v-list-item prepend-icon="mdi-cloud-upload-outline"
                     title="上传"
                     @click="UploadDialog = true">
        </v-list-item>
        <v-list-item prepend-icon="mdi-timeline-clock-outline"
                     title="时间线"
                     @click="openTimelineDialog">
        </v-list-item>
        <v-list-item prepend-icon="mdi-account-group-outline"
                     title="Users">
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-dialog
      v-model="TimelineDialog"
      transition="dialog-bottom-transition"
      fullscreen
      border
    >
      <v-card>
        <v-card-title>
          <v-btn
            icon="mdi-close"
            variant="text"
            @click="TimelineDialog = false"
          ></v-btn>
        </v-card-title>
        <div class="px-12 py-6">
          <v-timeline side="end">
            <v-timeline-item size="large"
                             dot-color="#2B2C40"
                             v-for="(event, i) in events"
                             :key="i">
              <template v-slot:icon>
                <span>📷️</span>
              </template>
              <template v-slot:opposite>
                <span>{{ event.title }}({{ event.count }})</span>
              </template>
              <v-card>
                <v-card-title>
                  {{ event.created_at }}
                </v-card-title>
                <v-card-text>
                  <v-btn text="查看" variant="text" class="mx-3"></v-btn>
                  <v-btn text="上传" variant="text" class="mx-3"></v-btn>
                </v-card-text>
              </v-card>
            </v-timeline-item>
          </v-timeline>
        </div>
      </v-card>
    </v-dialog>
    <v-dialog
      v-model="UploadDialog"
      width="40%"
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

  <v-fab
    icon="mdi-dots-grid"
    location="bottom right"
    size="60"
    app
    appear
    @click="drawer = true"
  ></v-fab>

</template>


<style scoped>
#gallery {
  flex: 1; /* 左侧区域 */
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
  gap: 1.5px;
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
