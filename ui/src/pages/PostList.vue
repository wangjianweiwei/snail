<script setup>
const items = []
for (let i = 0; i < 20; i++) {
  items.push({
    id: i,
    title: `${i}-MacOS M2 Tensorflow GPU环境搭建`,
    abstract: '介绍Stable Diffusion的图生图(img2img)。顾名思义，除了根据正向和反向提示词之外，还需要基于一张图片生成图。',
    create_at: "2024-07-21 15:43:35",
    category: "Jenkins",
    tags: ["cicd", 'deploy'],
  })
}
</script>

<template>
  <v-list>
    <v-list-item
      v-for="item in items"
      rounded="lg"
      class="my-2 pa-4"
      :key="item.id"
      :value="item.id"
      :title="item.title"
      :to="`/posts/${item.id}/preview`"
    >
      <v-list-item>
        <v-list-subheader>
          <div class="mt-3" style="font-size: 0.73rem;font-weight: 450">
            <span class="text-disabled mdi mdi-calendar-month-outline"></span>
            <span>发表于 {{ item.create_at }}</span>
            <v-divider
              class="ms-3"
              vertical
            ></v-divider>
            <span class="text-disabled mdi mdi-calendar-month-outline"></span>
            <span>更新于 {{ item.create_at }}</span>
          </div>
          <div class="mt-2">
            <v-chip class="mr-2" size="small">{{ item.category }}</v-chip>
            <v-chip class="mr-2" size="small" v-for="tag in item.tags">{{ tag }}</v-chip>
          </div>
        </v-list-subheader>
      </v-list-item>
    </v-list-item>
  </v-list>
  <div>
    <v-pagination :length="4"></v-pagination>
  </div>
</template>

<style scoped>

</style>
