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

const currentUser = 1
const avatars = {
  "1": "https://demos.themeselection.com/sneat-vuetify-vuejs-admin-template/demo-1/assets/avatar-1-DL1ARROH.png",
  "2": "https://cdn.vuetifyjs.com/images/lists/3.jpg"
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
const messages = [
  {"user_id": 1, "time": "2024/9/12 22:32:24", "message": {"type": "text", "content": "你好！"}},
  {"user_id": 2, "time": "2024/9/12 22:33:10", "message": {"type": "text", "content": "你好！有什么我可以帮忙的吗？"}},
  {
    "user_id": 1,
    "time": "2024/9/12 22:34:00",
    "message": {"type": "text", "content": "我在处理一个新项目，想了解一下如何更高效地管理团队。"}
  },
  {
    "user_id": 2,
    "time": "2024/9/12 22:35:15",
    "message": {"type": "text", "content": "这听起来不错。你现在的团队管理有哪些挑战呢？"}
  },
  {
    "user_id": 1,
    "time": "2024/9/12 22:36:00",
    "message": {"type": "text", "content": "主要是任务分配和进度跟踪。想找到一种方法来提高效率。"}
  },
  {
    "user_id": 2,
    "time": "2024/9/12 22:37:20",
    "message": {"type": "text", "content": "可以考虑使用一些任务管理工具或者制定更明确的流程规范。"}
  },
  {"user_id": 1, "time": "2024/9/12 22:38:00", "message": {"type": "text", "content": "你有推荐的工具吗？"}},
  {
    "user_id": 2,
    "time": "2024/9/12 22:39:10",
    "message": {"type": "text", "content": "像Jira或者Trello都挺好的，可以根据需求选择合适的工具。"}
  },
  {
    "user_id": 1,
    "time": "2024/9/12 22:40:00",
    "message": {"type": "text", "content": "我已经在使用Jira了，感觉还需要更多的自定义选项。"}
  },
  {
    "user_id": 2,
    "time": "2024/9/12 22:41:15",
    "message": {"type": "text", "content": "Jira确实有很多自定义选项，你可以尝试深入学习一下它的配置。"}
  },
  {
    "user_id": 1,
    "time": "2024/9/12 22:42:00",
    "message": {"type": "text", "content": "我还在考虑是否要引入更多的自动化工具来提高效率。"}
  },
  {
    "user_id": 2,
    "time": "2024/9/12 22:43:10",
    "message": {
      "type": "text",
      "content": "自动化工具确实可以帮助减少重复性工作。你可以试试一些常见的自动化解决方案，比如Zapier或者Integromat。"
    }
  },
  {
    "user_id": 1,
    "time": "2024/9/12 22:44:00",
    "message": {"type": "text", "content": "谢谢你的建议！我会去了解一下这些工具的。"}
  },
  {
    "user_id": 2,
    "time": "2024/9/12 22:45:05",
    "message": {"type": "text", "content": "不客气！如果有其他问题，随时找我。"}
  },
  {"user_id": 1, "time": "2024/9/12 22:46:00", "message": {"type": "text", "content": "好的，谢谢！"}},
  {
    "user_id": 2,
    "time": "2024/9/12 22:47:20",
    "message": {"type": "text", "content": "今天的讨论很有收获，希望你能顺利解决问题。"}
  },
  {"user_id": 1, "time": "2024/9/12 22:48:00", "message": {"type": "text", "content": "我也希望如此。晚安！"}},
  {"user_id": 2, "time": "2024/9/12 22:49:05", "message": {"type": "text", "content": "晚安！"}},
  {
    "user_id": 1,
    "time": "2024/9/13 09:15:00",
    "message": {"type": "text", "content": "早上好！我有个新的问题，关于如何优化团队的沟通方式。"}
  },
  {
    "user_id": 2,
    "time": "2024/9/13 09:16:20",
    "message": {"type": "text", "content": "早上好！沟通方式的优化可以考虑定期召开团队会议，使用统一的沟通工具等。"}
  },
  {
    "user_id": 1,
    "time": "2024/9/13 09:17:00",
    "message": {"type": "text", "content": "我们目前使用Slack进行沟通，但感觉信息比较分散。"}
  },
  {
    "user_id": 2,
    "time": "2024/9/13 09:18:15",
    "message": {"type": "text", "content": "可以试试设置一些频道来分类信息，或者利用Slack的搜索功能更好地找到信息。"}
  },
  {"user_id": 1, "time": "2024/9/13 09:19:00", "message": {"type": "text", "content": "好的，我会去尝试一下。谢谢！"}},
  {
    "user_id": 2,
    "time": "2024/9/13 09:20:05",
    "message": {"type": "text", "content": "不客气！如果有任何问题，随时联系我。"}
  },
  {
    "user_id": 1,
    "time": "2024/9/13 10:00:00",
    "message": {"type": "text", "content": "另外，我需要一些关于如何评估团队绩效的建议。"}
  },
  {
    "user_id": 2,
    "time": "2024/9/13 10:01:20",
    "message": {"type": "text", "content": "评估团队绩效可以通过定期的绩效评估，设定明确的目标和关键绩效指标来实现。"}
  },
  {
    "user_id": 1,
    "time": "2024/9/13 10:02:00",
    "message": {"type": "text", "content": "目标设定方面有什么具体的方法吗？"}
  },
  {
    "user_id": 2,
    "time": "2024/9/13 10:03:15",
    "message": {"type": "text", "content": "可以使用SMART原则来设定目标，确保目标具体、可测量、可实现、相关和有时限。"}
  },
  {"user_id": 1, "time": "2024/9/13 10:04:00", "message": {"type": "text", "content": "明白了。谢谢你的帮助！"}},
  {"user_id": 2, "time": "2024/9/13 10:05:05", "message": {"type": "text", "content": "不客气，祝你工作顺利！"}},
  {
    "user_id": 1,
    "time": "2024/9/13 10:30:00",
    "message": {"type": "text", "content": "还有一个问题，我在考虑如何提高团队的创新能力。"}
  },
  {
    "user_id": 2,
    "time": "2024/9/13 10:31:20",
    "message": {"type": "text", "content": "可以通过鼓励团队成员提出新想法，设立创新奖励机制来提升创新能力。"}
  },
  {
    "user_id": 1,
    "time": "2024/9/13 10:32:00",
    "message": {"type": "text", "content": "这些建议听起来不错，我会尝试实施。"}
  },
  {
    "user_id": 2,
    "time": "2024/9/13 10:33:10",
    "message": {"type": "text", "content": "很高兴能帮到你。如果有任何新的问题，随时告诉我。"}
  }
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
              <v-sheet class="pa-3 align-center d-flex justify-space-between">
                <div>
                  <v-list
                    density="comfortable"
                    lines="two"
                    variant="elevated"
                  >
                    <v-list-item
                      prepend-avatar="https://cdn.vuetifyjs.com/images/lists/3.jpg"
                      title="Harriet McBride"
                      subtitle="UI/UX Designer"
                    >

                    </v-list-item>
                  </v-list>
                </div>
                <div>
                  <v-btn icon="mdi-phone-outline" variant="text" color=""></v-btn>
                  <v-btn icon="mdi-video-outline" variant="text" color=""></v-btn>
                  <v-btn icon="mdi-magnify" variant="text" color=""></v-btn>
                  <v-btn icon="mdi-dots-vertical" variant="text" color=""></v-btn>
                </div>
              </v-sheet>
            </v-col>
          </v-row>
          <v-row no-gutters style="height: 92%">
            <v-col cols="3" style="overflow-y: scroll">
              <v-list
                activatable
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
                <v-col class="pa-3" style="overflow-y: scroll">
                  <v-list
                    bg-color="#20202e"
                  >
                    <v-list-item
                      v-for="(n, i) in messages"
                      :key="i"
                      :class="{'text-right': n.user_id === currentUser, 'text-left': n.user_id !== currentUser}"
                      :prepend-avatar="n.user_id === currentUser ? '' : avatars[n.user_id]"
                      :append-avatar="n.user_id === currentUser ? avatars[n.user_id] : ''"
                    >
                      <template #title>
                        <p class="text-md-body-1 rounded-lg pa-2 mb-2 message-content font-weight-regular"
                           :style="{'background-color': n.user_id === currentUser?'#696CFF': '#2b2c40'}">
                          {{ n.message.content }}</p>
                      </template>
                      <template #subtitle>
                        <div style="font-size: 0.8rem;font-weight: 500">
                          <v-icon v-if="currentUser === n.user_id" size="sm" icon="mdi-check-bold" color="success"
                                  class="mr-1"></v-icon>
                          <span>{{ n.time }}</span>
                        </div>

                      </template>
                    </v-list-item>
                  </v-list>
                </v-col>
              </v-row>
              <v-row no-gutters style="height: 10%;background-color: #20202e">
                <v-col>
                  <v-sheet class="pa-3" style="background-color: #20202e">
                    <v-text-field variant="solo-filled" no-resize center-affix>
                      <template #append-inner>
                        <v-btn icon="mdi-microphone-outline" variant="text" color=""></v-btn>
                        <v-btn icon="mdi-attachment" variant="text" color=""></v-btn>
                        <v-btn icon="mdi-emoticon-outline" variant="text" color=""></v-btn>
                        <v-btn icon="mdi-send-outline" variant="text" color=""></v-btn>
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

.message-content {
  display: inline-block;
  color: #dbdbeb;
}
</style>
