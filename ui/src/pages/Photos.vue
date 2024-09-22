<script setup>

import {ref, onMounted} from "vue";
import Viewer from "viewerjs";
import 'viewerjs/dist/viewer.css';

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
  <div id="preview"></div>
  <div id="gallery">
    <div class="gallery-item" v-for="n in images">
      <img :src="n" alt="12">
    </div>
  </div>
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
