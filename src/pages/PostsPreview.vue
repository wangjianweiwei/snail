<script setup>
const category = [
  {text: 'All(53)', icon: 'mdi-clock'},
  {text: 'Real-Time(20)', icon: 'mdi-clock'},
  {text: 'Audience(8)', icon: 'mdi-account'},
  {text: 'Conversions(17)', icon: 'mdi-flag'},
]
</script>

<template>
  <div class="px-12 py-6">
    <v-row>
      <v-col cols="9" class="my-4">
        <p>12</p>
        <p>12</p>
        <p>12</p>
        <p>12</p>
        <p>12</p>
        <p>12</p>
        <p>12</p>
        <p>12</p>
        <p>12</p>
        <p>12</p>
        <p>12</p>
        <p>12</p>
        <p>12</p>
        <p>12</p>
        <p>12d</p>
        <p>12</p>
        <p>12</p>
        <p>12</p>
        <p>12</p>
        <p>12</p>
        <p>12</p>
        <p>12</p>
        <p>12</p>
        <p>12</p>
        <p>12</p>
        <p>12</p>
        <p>12d</p>
        <p>12</p>
        <p>12</p>
        <p>12</p>
        <p>12</p>
        <p>12</p>
        <p>12</p>
        <p>12</p>
        <p>12</p>
        <p>12</p>
        <p>12</p>
        <p>12</p>
        <p>12d</p>
        <p>12</p>
        <p>12</p>
        <p>12</p>
        <p>12</p>
        <p>12</p>
        <p>12</p>
        <p>12</p>
        <p>12</p>
        <p>12</p>
        <p>12</p>
        <p>12</p>
        <p>12d</p>

      </v-col>
      <v-col cols="3">

        <div class="position-fixed">
          <v-btn icon="mdi-circle-edit-outline" variant="text" to="/dashboards/posts/0/compose">
            <v-icon icon="mdi-circle-edit-outline"></v-icon>
            <v-tooltip
              activator="parent"
              location="top"
              text="编辑"
            >
            </v-tooltip>
          </v-btn>
          <v-btn icon="mdi-cloud-upload-outline" variant="text">
            <v-icon icon="mdi-cloud-upload-outline"></v-icon>
            <v-tooltip
              activator="parent"
              location="top"
              text="发布"
            >
            </v-tooltip>
          </v-btn>
          <v-btn icon="mdi-undo-variant" variant="text">
            <v-icon icon="mdi-undo-variant"></v-icon>
            <v-tooltip
              activator="parent"
              location="top"
              text="下架"
            >
            </v-tooltip>
          </v-btn>
          <v-list rounded="lg" variant="text" bg-color="#232332">
            <v-list-subheader>目录</v-list-subheader>
            <v-list-item
              v-for="(item, i) in category"
              rounded="lg"
              :key="i"
              :value="item"
            >
              <v-list-item-subtitle v-text="item.text"></v-list-item-subtitle>
              <template></template>

            </v-list-item>
          </v-list>
        </div>
      </v-col>

    </v-row>

  </div>
</template>

<style scoped lang="sass">

</style>
