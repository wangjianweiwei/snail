<script setup>
import {ref, reactive, nextTick, onMounted} from "vue";
import {no, tr} from "vuetify/locale";
import moment from "moment";

moment.locale('zh-cn');

const drawer = ref(false)
const drawerWidth = ref(0)
const currentMsg = ref("")
const currentUser = reactive({
  id: 1,
  status: "success",
  settings: {
    two_step: false,
    notify: false
  },
  avatar: "https://demos.themeselection.com/sneat-vuetify-vuejs-admin-template/demo-1/assets/avatar-1-DL1ARROH.png"
})
const friend = ref(null)
const friends = [
  {
    prependAvatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
    title: 'Gavin Griffith',
    value: 1,
    subtitle: "I will purchase it for sure. 👍",
  },
  {
    prependAvatar: 'https://cdn.vuetifyjs.com/images/lists/2.jpg',
    title: 'Harriet McBride',
    value: 2,
    subtitle: "If it takes long you can mail me at m",
  },
  {
    prependAvatar: 'https://cdn.vuetifyjs.com/images/lists/3.jpg',
    title: 'Danny Conner',
    value: 3,
    subtitle: 'Cake pie jelly jelly beans. Marzipan lemon dr',
  },
  {
    prependAvatar: 'https://cdn.vuetifyjs.com/images/lists/4.jpg',
    title: 'Janie West',
    value: 4,
    subtitle: 'Chupa chups candy canes chocolate bar mar',
  },
  {
    prependAvatar: 'https://cdn.vuetifyjs.com/images/lists/5.jpg',
    title: 'Albert Underwood',
    value: 5,
    subtitle: 'Toffee caramels jelly-o tart gummi bears ca',
  },
  {
    prependAvatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
    title: 'Gavin Griffith',
    value: 6,
    subtitle: "I will purchase it for sure. 👍",
  },
  {
    prependAvatar: 'https://cdn.vuetifyjs.com/images/lists/2.jpg',
    title: 'Harriet McBride',
    value: 7,
    subtitle: "If it takes long you can mail me at m",
  },
  {
    prependAvatar: 'https://cdn.vuetifyjs.com/images/lists/3.jpg',
    title: 'Danny Conner',
    value: 8,
    subtitle: 'Cake pie jelly jelly beans. Marzipan lemon dr',
  },
  {
    prependAvatar: 'https://cdn.vuetifyjs.com/images/lists/4.jpg',
    title: 'Janie West',
    value: 9,
    subtitle: 'Chupa chups candy canes chocolate bar mar',
  },
  {
    prependAvatar: 'https://cdn.vuetifyjs.com/images/lists/5.jpg',
    title: 'Albert Underwood',
    value: 10,
    subtitle: 'Toffee caramels jelly-o tart gummi bears ca',
  },
  {
    prependAvatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
    title: 'Gavin Griffith',
    value: 11,
    subtitle: "I will purchase it for sure. 👍",
  },
  {
    prependAvatar: 'https://cdn.vuetifyjs.com/images/lists/2.jpg',
    title: 'Harriet McBride',
    value: 12,
    subtitle: "If it takes long you can mail me at m",
  },
  {
    prependAvatar: 'https://cdn.vuetifyjs.com/images/lists/3.jpg',
    title: 'Danny Conner',
    value: 13,
    subtitle: 'Cake pie jelly jelly beans. Marzipan lemon dr',
  },
  {
    prependAvatar: 'https://cdn.vuetifyjs.com/images/lists/4.jpg',
    title: 'Janie West',
    value: 14,
    subtitle: 'Chupa chups candy canes chocolate bar mar',
  },
  {
    prependAvatar: 'https://cdn.vuetifyjs.com/images/lists/5.jpg',
    title: 'Albert Underwood',
    value: 15,
    subtitle: 'Toffee caramels jelly-o tart gummi bears ca',
  },
]
const messages = ref({
  "1": [
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
    {
      "user_id": 1,
      "time": "2024/9/13 10:04:00",
      "loading": true,
      "message": {"type": "text", "content": "明白了。谢谢你的帮助！"}
    },
    {"user_id": 2, "time": "2024/9/13 10:05:05", "message": {"type": "text", "content": "不客气，祝你工作顺利！"}}
  ],
  "2": [
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
      "loading": true,
      "message": {"type": "text", "content": "这些建议听起来不错，我会尝试实施。"}
    },
    {
      "user_id": 2,
      "time": "2024/9/13 10:33:10",
      "message": {"type": "text", "content": "很高兴能帮到你。如果有任何新的问题，随时告诉我。"}
    }
  ],
  "3": [
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
      "loading": true,
      "message": {"type": "text", "content": "这些建议听起来不错，我会尝试实施。"}
    },
  ],
  "4": [
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
      "loading": true,
      "message": {"type": "text", "content": "这些建议听起来不错，我会尝试实施。"}
    },
    {
      "user_id": 2,
      "time": "2024/9/13 10:33:10",
      "message": {"type": "text", "content": "很高兴能帮到你。如果有任何新的问题，随时告诉我。"}
    }
  ]
})

const load = ({done}) => {
  setTimeout(() => {
    messages.value[friend.value.value].unshift({
      "user_id": 1,
      "time": "2024/9/12 22:32:24",
      "message": {"type": "text", "content": "你好！"}
    })
    done("ok")
  }, 2000)

}
const SelectFriend = (v) => {
  friend.value = friends.find((x) => {
    return x.value === v.id
  })
}

const updateDrawerWidth = () => {
  drawerWidth.value = window.document.getElementById("avatarCol").getBoundingClientRect().width + 3
}

const sendMsg = () => {
  let now = new moment().format('YYYY/MM/DD HH:mm:ss')
  messages.value.push({
    "user_id": 1,
    "time": now,
    "message": {"type": "text", "content": currentMsg.value}
  },)
  console.log(currentMsg.value)
  currentMsg.value = ""
}


</script>

<template>
  <div style="height: 100%" class="py-lg-5">
    <v-layout style="height: 100%">
      <v-row justify="center" no-gutters style="height: 100%">
        <v-col lg="10" xl="9">
          <v-card rounded="lg" style="height: 100%" border>
            <!--头部区域-->
            <v-row no-gutters style="height: 10%" align="center">
              <!--我的头像区域-->
              <v-col id="avatarCol"
                     cols="3"
                     style="height: 100%"
                     class="pa-4 border-b-sm d-flex justify-start align-center"
                     v-resize="updateDrawerWidth">
                <v-navigation-drawer
                  absolute
                  v-model="drawer"
                  :width="drawerWidth"
                  temporary
                >
                  <div class="px-4 py-3">
                    <div class="d-flex justify-end">
                      <v-btn icon="mdi-close"
                             variant="text"
                             size="small" @click="drawer = false"></v-btn>
                    </div>
                    <div class="text-center">
                      <v-badge dot location="bottom end" :color="currentUser.status">
                        <v-avatar :image="currentUser.avatar" size="70" variant="flat"></v-avatar>
                      </v-badge>
                      <p class="text-h6">John Doe</p>
                      <p class="text-capitalize text-body-2 mb-0">develop</p>
                    </div>
                    <div class="mt-5">
                      <p class="text-disabled mb-1">状态</p>
                      <v-radio-group v-model="currentUser.status">
                        <v-radio label="在线" value="success" density="comfortable" color="success"></v-radio>
                        <v-radio label="离开" value="warning" density="comfortable" color="warning"></v-radio>
                        <v-radio label="请勿打扰" value="error" density="comfortable" color="error"></v-radio>
                        <v-radio label="离线" value="grey" density="comfortable" color="grey"></v-radio>
                      </v-radio-group>
                    </div>
                    <div class="mt-5">
                      <p class="text-disabled mb-1">设置</p>
                      <div class="d-flex justify-space-between align-center px-2">
                        <div class="d-flex justify-start">
                          <v-icon size="small" icon="mdi-lock-outline"></v-icon>
                          <p class="text-body-1 ml-2 text-high-emphasis">两步验证</p>
                        </div>
                        <v-switch density="compact" center-affix v-model="currentUser.settings.two_step"></v-switch>
                      </div>
                      <div class="d-flex justify-space-between align-center px-2">
                        <div class="d-flex justify-start">
                          <v-icon size="small" icon="mdi-bell-outline"></v-icon>
                          <p class="text-body-1 ml-2 text-high-emphasis">通知</p>
                        </div>
                        <v-switch density="compact" center-affix v-model="currentUser.settings.notify"></v-switch>
                      </div>
                      <div class="d-flex justify-space-between align-center px-2">
                        <div class="d-flex justify-start">
                          <v-icon size="small" icon="mdi-account-plus-outline"></v-icon>
                          <p class="text-body-1 ml-2 text-high-emphasis">邀请朋友</p>
                        </div>
                        <v-switch style="visibility: hidden" density="compact" center-affix></v-switch>
                      </div>
                      <div class="d-flex justify-space-between align-center px-2">
                        <div class="d-flex justify-start text-subtitle-2">
                          <v-icon size="small" icon="mdi-delete-outline"></v-icon>
                          <p class="text-body-1 ml-2 text-high-emphasis">删除账户</p>
                        </div>
                        <v-switch style="visibility: hidden" density="compact" center-affix hide-details></v-switch>
                      </div>

                    </div>
                    <div class="mt-5">
                      <v-btn block prepend-icon="mdi-logout">退出登录</v-btn>
                    </div>
                  </div>
                </v-navigation-drawer>
                <v-badge dot location="bottom end" :color="currentUser.status">
                  <v-avatar @click="drawer = true" :image="currentUser.avatar"></v-avatar>
                </v-badge>
              </v-col>
              <v-divider vertical></v-divider>
              <!--好友工具栏区域-->
              <v-col v-if="friend"
                     cols="9"
                     style="height: 100%"
                     class="border-b-sm pa-4 align-center d-flex justify-space-between">
                <v-list-item
                  :prepend-avatar="friend.prependAvatar"
                  :title="friend.title"
                  subtitle="UI/UX Designer"
                >
                </v-list-item>
                <div>
                  <v-btn icon="mdi-phone-outline" variant="text" color=""></v-btn>
                  <v-btn icon="mdi-video-outline" variant="text" color=""></v-btn>
                  <v-btn icon="mdi-magnify" variant="text" color=""></v-btn>
                  <v-btn icon="mdi-dots-vertical" variant="text" color=""></v-btn>
                </div>
              </v-col>
              <!--空白好友工具栏区域-->
              <v-col v-else style="height: 100%"></v-col>
            </v-row>
            <!--底部区域-->
            <v-row no-gutters style="height: 90%">
              <!--好友列表区域-->
              <v-col cols="3" style="overflow-y: scroll">
                <v-list
                  activatable
                  :items="friends"
                  lines="two"
                  item-props
                  variant="elevated"
                  @click:activate="SelectFriend"
                >
                  <template v-slot:subtitle="{ subtitle }">
                    <p class="text-truncate mt-1">{{ subtitle }}</p>
                  </template>
                  <template v-slot:append="{ item }">
                    <div class="d-flex flex-column align-self-start text-center">
                      <span class="text-disabled" style="font-size: 0.73rem;font-weight: 450">23:30:50</span>

                      <v-badge class="mt-1" v-if="item.value === 1" inline content="99+" color="red-darken-2"></v-badge>
                    </div>
                  </template>
                </v-list>
              </v-col>
              <v-divider vertical></v-divider>
              <!--聊天区域-->
              <v-col v-if="friend" cols="9" style="height: 100%">
                <!--消息记录区域-->
                <v-row no-gutters style="height: 90%">
                  <v-col class="px-3">
                    <v-infinite-scroll height="100%" side="start" @load="load">
                      <template #default>
                        <v-list-item
                          v-for="(n, i) in messages[friend.value]"
                          :key="i"
                          :class="{'text-right': n.user_id === currentUser.id, 'text-left': n.user_id !== currentUser.id}"

                        >
                          <template #title>
                            <v-progress-circular v-if="currentUser.id === n.user_id && n.loading" width="2" size="13"
                                                 class="mr-2"
                                                 indeterminate></v-progress-circular>
                            <p class="text-sm-body-2 rounded-lg pa-2 mb-2 message-content font-weight-medium"
                               :style="{'background-color': n.user_id === currentUser.id ? '#696CFF': '#2b2c40'}">
                              {{ n.message.content }}</p>
                          </template>
                          <template #append v-if="n.user_id === currentUser.id">
                            <v-avatar size="small" :image="currentUser.avatar"></v-avatar>
                          </template>
                          <template #prepend v-if="n.user_id !== currentUser.id">
                            <v-avatar size="small" :image="friend.prependAvatar"></v-avatar>
                          </template>
                          <template #subtitle>
                            <div class="text-disabled" style="font-size: 0.73rem;font-weight: 450">
                              <v-icon v-if="currentUser.id === n.user_id"
                                      icon="mdi-check-bold"
                                      color="success"
                                      class="mr-1"></v-icon>
                              <span>{{ n.time }}</span>
                            </div>

                          </template>
                        </v-list-item>
                      </template>
                    </v-infinite-scroll>
                  </v-col>
                </v-row>
                <!--消息发送区域-->
                <v-row no-gutters style="height: 10%" align="center">
                  <v-col class="pa-4">
                    <v-sheet>
                      <v-text-field v-model="currentMsg" variant="solo-filled" no-resize
                                    center-affix @keydown.enter="sendMsg">
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
              <!--空白聊天区域-->
              <v-col v-else cols="9" style="height: 100%"
                     class="d-flex flex-column justify-center align-center">
                <v-icon size="100" icon="mdi-message-question-outline" class="mb-2"></v-icon>
                <p class="text-grey-darken-1 text-sm-body-2 font-weight-black">选择左侧的联系人开始联系</p>
              </v-col>
            </v-row>
          </v-card>
        </v-col>
      </v-row>
    </v-layout>
  </div>
</template>

<style scoped>
.v-row {
  flex-wrap: nowrap;
}


/* 针对 WebKit 浏览器 (如 Chrome, Safari, Edge) */
::-webkit-scrollbar {
  width: 3px; /* 滚动条的宽度 */
  height: 3px; /* 滚动条的高度（用于水平滚动条） */
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

.v-navigation-drawer {
  transition-duration: 0.5s !important; /* 自定义过渡时间 */
}
</style>

