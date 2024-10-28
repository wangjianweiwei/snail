<template>
  <div class="py-lg-5">
    <v-layout>
      <v-row justify="center">
        <v-col cols="2">
          <v-row>
            <v-col cols="12">
              <v-sheet rounded="lg" elevation="12">
                <v-list density="compact" lines="one" rounded="lg">
                  <v-list-item
                    rounded="lg"
                    class="mx-2 my-1"
                    value="首页"
                    subtitle="首页"
                    prepend-icon="mdi-page-first"
                  >
                  </v-list-item>
                  <v-list-item
                    value="分类"
                    class="mx-2 my-1"
                    rounded="lg"
                    subtitle="分类"
                    prepend-icon="mdi-view-grid-plus-outline"
                  >
                  </v-list-item>
                  <v-list-item
                    value="标签"
                    class="mx-2 my-1"
                    rounded="lg"
                    subtitle="标签"
                    prepend-icon="mdi-tag-outline"
                  >
                  </v-list-item>
                  <v-list-item
                    value="时间线"
                    class="mx-2 my-1"
                    rounded="lg"
                    subtitle="时间线"
                    prepend-icon="mdi-timeline-check-outline"
                  >
                  </v-list-item>
                </v-list>
              </v-sheet>
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
            <v-list>
              <v-list-item
                v-for="item in items"
                rounded="lg"
                class="my-2 pa-4"
                :key="item.id"
                :value="item.id"
                :title="item.title"
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
          </v-sheet>
        </v-col>
      </v-row>
    </v-layout>
  </div>

</template>

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
