<script setup>
import {ref} from "vue";

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

const friends = [
  {type: 'subheader', title: 'Today'},
  {
    prependAvatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
    title: 'Brunch this weekend?',
    value: 1,
    subtitle: `<span class="text-primary">Ali Connors</span> &mdash; I'll be in your neighborhood doing errands this weekend. Do you want to hang out?`,
  },
  {
    prependAvatar: 'https://cdn.vuetifyjs.com/images/lists/2.jpg',
    title: 'Summer BBQ',
    value: 2,
    subtitle: `<span class="text-primary">to Alex, Scott, Jennifer</span> &mdash; Wish I could come, but I'm out of town this weekend.`,
  },
  {
    prependAvatar: 'https://cdn.vuetifyjs.com/images/lists/3.jpg',
    title: 'Oui oui',
    value: 3,
    subtitle: '<span class="text-primary">Sandra Adams</span> &mdash; Do you have Paris recommendations? Have you ever been?',
  },
  {
    prependAvatar: 'https://cdn.vuetifyjs.com/images/lists/4.jpg',
    title: 'Birthday gift',
    value: 4,
    subtitle: '<span class="text-primary">Trevor Hansen</span> &mdash; Have any ideas about what we should get Heidi for her birthday?',
  },
  {
    prependAvatar: 'https://cdn.vuetifyjs.com/images/lists/5.jpg',
    title: 'Recipe to try',
    value: 5,
    subtitle: '<span class="text-primary">Britta Holt</span> &mdash; We should eat this: Grate, Squash, Corn, and tomatillo Tacos.',
  },
  {
    prependAvatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
    title: 'Brunch this weekend?',
    value: 6,
    subtitle: `<span class="text-primary">Ali Connors</span> &mdash; I'll be in your neighborhood doing errands this weekend. Do you want to hang out?`,
  },
  {
    prependAvatar: 'https://cdn.vuetifyjs.com/images/lists/2.jpg',
    title: 'Summer BBQ',
    value: 7,
    subtitle: `<span class="text-primary">to Alex, Scott, Jennifer</span> &mdash; Wish I could come, but I'm out of town this weekend.`,
  },
  {
    prependAvatar: 'https://cdn.vuetifyjs.com/images/lists/3.jpg',
    title: 'Oui oui',
    value: 8,
    subtitle: '<span class="text-primary">Sandra Adams</span> &mdash; Do you have Paris recommendations? Have you ever been?',
  },
  {
    prependAvatar: 'https://cdn.vuetifyjs.com/images/lists/4.jpg',
    title: 'Birthday gift',
    value: 9,
    subtitle: '<span class="text-primary">Trevor Hansen</span> &mdash; Have any ideas about what we should get Heidi for her birthday?',
  },
  {
    prependAvatar: 'https://cdn.vuetifyjs.com/images/lists/5.jpg',
    title: 'Recipe to try',
    value: 10,
    subtitle: '<span class="text-primary">Britta Holt</span> &mdash; We should eat this: Grate, Squash, Corn, and tomatillo Tacos.',
  },
  {
    prependAvatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
    title: 'Brunch this weekend?',
    value: 11,
    subtitle: `<span class="text-primary">Ali Connors</span> &mdash; I'll be in your neighborhood doing errands this weekend. Do you want to hang out?`,
  },
  {
    prependAvatar: 'https://cdn.vuetifyjs.com/images/lists/2.jpg',
    title: 'Summer BBQ',
    value: 12,
    subtitle: `<span class="text-primary">to Alex, Scott, Jennifer</span> &mdash; Wish I could come, but I'm out of town this weekend.`,
  },
  {
    prependAvatar: 'https://cdn.vuetifyjs.com/images/lists/3.jpg',
    title: 'Oui oui',
    value: 13,
    subtitle: '<span class="text-primary">Sandra Adams</span> &mdash; Do you have Paris recommendations? Have you ever been?',
  },
  {
    prependAvatar: 'https://cdn.vuetifyjs.com/images/lists/4.jpg',
    title: 'Birthday gift',
    value: 14,
    subtitle: '<span class="text-primary">Trevor Hansen</span> &mdash; Have any ideas about what we should get Heidi for her birthday?',
  },
  {
    prependAvatar: 'https://cdn.vuetifyjs.com/images/lists/5.jpg',
    title: 'Recipe to try',
    value: 15,
    subtitle: '<span class="text-primary">Britta Holt</span> &mdash; We should eat this: Grate, Squash, Corn, and tomatillo Tacos.',
  },
]
</script>

<template>
  <div style="height: 100%" class="py-8">
    <v-row justify="center" no-gutters style="height: 100%">
      <v-col lg="10" xl="8">
        <v-card rounded="lg" style="height: 100%">
          <v-row no-gutters style="height: 8%" class="border-b-sm" align="center">
            <v-col cols="3">
              <v-sheet class="pa-3 d-flex justify-start">
                <v-avatar
                  image="https://demos.themeselection.com/sneat-vuetify-vuejs-admin-template/demo-1/assets/avatar-1-DL1ARROH.png"></v-avatar>
                <v-text-field class="ms-4" rounded="xl" prepend-inner-icon="mdi-magnify" density="compact"
                              placeholder="Search"></v-text-field>
              </v-sheet>
            </v-col>
            <v-divider vertical></v-divider>
            <v-col cols="9">
              <v-sheet class="pa-3 align-center">
                <p>对话工具栏</p>
              </v-sheet>
            </v-col>
          </v-row>
          <v-row no-gutters style="height: 92%">
            <v-col cols="3" style="overflow-y: scroll">
              <v-list
                density="comfortable"
                :items="friends"
                lines="two"
                item-props
                variant="elevated"
              >
                <template v-slot:subtitle="{ subtitle }">
                  <div v-html="subtitle"></div>
                </template>
              </v-list>
            </v-col>
            <v-divider vertical></v-divider>
            <v-col cols="9" style="height: 100%">
              <v-row no-gutters style="height: 90%;background-color: #20202e">
                <v-col class="pa-6" style="overflow-y: scroll">
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                  <p>聊天内容</p>
                </v-col>
              </v-row>
              <v-row no-gutters style="height: 10%;background-color: #20202e">
                <v-col>
                  <v-sheet class="pa-3" style="background-color: #20202e">
                    <v-text-field variant="solo-filled" no-resize center-affix>
                      <template #append-inner>
                        <v-btn icon="mdi-microphone-outline" variant="text"></v-btn>
                        <v-btn icon="mdi-attachment" variant="text"></v-btn>
                        <v-btn rounded="lg">发送</v-btn>
                      </template>
                    </v-text-field>
                  </v-sheet>
                </v-col>
              </v-row>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<style scoped>
.v-row {
  flex-wrap: nowrap;
}

.v-field__append-inner {
  align-items: center;
}

/* 针对 WebKit 浏览器 (如 Chrome, Safari, Edge) */
::-webkit-scrollbar {
  width: 1px; /* 滚动条的宽度 */
  height: 8px; /* 滚动条的高度（用于水平滚动条） */
}

::-webkit-scrollbar-track {
  background: #2e2e2e; /* 滚动条轨道的背景色 */
  border-radius: 4px; /* 圆角 */
}

::-webkit-scrollbar-thumb {
  background-color: #555; /* 滚动条滑块的颜色 */
  border-radius: 4px; /* 滑块的圆角 */
  border: 2px solid #2e2e2e; /* 为滑块加上边框以显示间隙 */
}

::-webkit-scrollbar-thumb:hover {
  background-color: #777; /* 滑块在悬停时的颜色 */
}

::-webkit-scrollbar-thumb:active {
  background-color: #999; /* 滑块在点击时的颜色 */
}

/* 针对 Firefox 浏览器 */
* {
  scrollbar-width: thin; /* 滚动条的宽度 */
  scrollbar-color: #555 #2e2e2e; /* 滑块颜色 #555 和轨道颜色 #2e2e2e */
}


</style>
