<template>
  <div class="px-12 py-6">
    <v-row>
      <v-col cols="2" class="my-4">
        <v-card class="position-fixed">
          <v-list rounded="lg" variant="text" bg-color="#232332">
            <v-list-subheader>分类</v-list-subheader>
            <v-list-item
              v-for="(item, i) in category"
              :key="i"
              rounded="lg"
              :value="item"
            >
              <v-list-item-subtitle v-text="item.text"></v-list-item-subtitle>
            </v-list-item>
          </v-list>
        </v-card>
      </v-col>
      <v-col cols="10">
        <v-hover v-for="item in items">
          <template #default="{ isHovering, props }">
            <v-card
              v-bind="props"
              :color="isHovering ? 'primary': ''"
              rounded="lg"
              :variant="isHovering ? 'flat' : 'text'"
              class="my-4"
              :key="item.id"

            >
              <v-card-item>
                <v-card-title>
                  {{ item.title }}
                </v-card-title>

                <v-card-subtitle>
                  <span>{{ item.create_at }}</span>
                  <v-chip class="ma-2">{{ item.category }}</v-chip>
                  <v-chip class="ma-2" v-for="tag in item.tags">{{ tag }}</v-chip>
                </v-card-subtitle>
              </v-card-item>

              <v-card-text>
                {{ item.abstract }}
              </v-card-text>
              <v-card-actions>
                <v-btn color="" variant="text" border :to="`/dashboards/posts/${item.id}/preview`">阅读全文</v-btn>
              </v-card-actions>
            </v-card>
            <v-divider></v-divider>
          </template>
        </v-hover>
        <v-fab
          icon="mdi-plus"
          class="mb-4"
          location="bottom right"
          size="50"
          app
          appear
        >
          <v-icon icon="mdi-plus"></v-icon>
          <v-dialog activator="parent" max-width="500">
            <template v-slot:default="{ isActive }">
              <v-card rounded="lg">
                <v-card-title>
                  新建文章
                </v-card-title>

                <v-card-text>
                  <v-text-field density="compact" label="文章名称" variant="outlined"></v-text-field>
                </v-card-text>

                <v-card-actions>
                  <v-btn
                    text="创建"
                    @click="isActive.value = false"
                  ></v-btn>
                </v-card-actions>
              </v-card>
            </template>
          </v-dialog>
        </v-fab>
      </v-col>
    </v-row>

  </div>

</template>

<script setup>

const items = []
for (let i = 0; i < 20; i++) {
  items.push({
    id: i,
    title: `${i}-Brunch this weekend?`,
    abstract: '介绍Stable Diffusion的图生图(img2img)。顾名思义，除了根据正向和反向提示词之外，还需要基于一张图片生成图。',
    create_at: "2024-07-21 15:43:35",
    category: "Jenkins",
    tags: ["cicd", 'deploy'],
  })
}
const category = [
    { text: 'All(53)', icon: 'mdi-clock' },
    { text: 'Real-Time(20)', icon: 'mdi-clock' },
    { text: 'Audience(8)', icon: 'mdi-account' },
    { text: 'Conversions(17)', icon: 'mdi-flag' },
  ]
const debug = (a) => {
  console.log(a)

}
</script>
