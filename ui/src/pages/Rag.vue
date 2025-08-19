<script setup>
import {reactive, ref, onMounted, nextTick} from "vue";
import {q} from '@/services'
import {baseURL} from "@/config";

const messages = reactive([])
const currentMsg = ref("")
const talk_id = ref("")
const chatContainer = ref(null);


function uuid() {
  var s = [];
  var hexDigits = "0123456789abcdef";
  for (var i = 0; i < 36; i++) {
    s[i] = hexDigits.substr(Math.floor(Math.random() * 0x10), 1);
  }
  s[14] = "4"; // bits 12-15 of the time_hi_and_version field to 0010
  s[19] = hexDigits.substr((s[19] & 0x3) | 0x8, 1); // bits 6-7 of the clock_seq_hi_and_reserved to 01
  s[8] = s[13] = s[18] = s[23] = "-";

  return s.join("");
}

function getCurrentTime() {
  const now = new Date();

  const year = now.getFullYear();
  const month = String(now.getMonth() + 1).padStart(2, "0"); // 月份补零
  const day = String(now.getDate()).padStart(2, "0");        // 日补零
  const hour = String(now.getHours()).padStart(2, "0");       // 时补零
  const minute = String(now.getMinutes()).padStart(2, "0");   // 分补零
  const second = String(now.getSeconds()).padStart(2, "0");   // 秒补零

  return `${year}-${month}-${day} ${hour}:${minute}:${second}`;
}

async function sendMsg() {
  if (!currentMsg.value.trim()) {
    return
  }
  messages.push({
    user: currentMsg.value,
    ai: "",
    userTime: getCurrentTime(),
    aiLoading: true,
    userLoading: true
  })
  await q(talk_id.value, currentMsg.value)
  messages[messages.length - 1].userLoading = false
  currentMsg.value = ""
  await nextTick()
  updateChatContainerHeight()

}

function updateChatContainerHeight() {
  const el = chatContainer.value?.$el
  el.scrollTop = el.scrollHeight - el.clientHeight;
}

onMounted(() => {
  talk_id.value = uuid()
  const eventSource = new EventSource(`${baseURL}/api/rag/sse?talk_id=${talk_id.value}`);

  eventSource.onopen = () => {
    console.log('Connection to server opened.')
  };

  eventSource.onmessage = (event) => {
    const msgLength = messages.length
    const lastMsg = messages[msgLength - 1]
    messages[msgLength - 1] = {
      ...lastMsg,
      ai: lastMsg.ai + event.data,
      aiLoading: false,
      aiTime: getCurrentTime(),
    }
    nextTick(() => {
      updateChatContainerHeight()
    })

  }

  eventSource.onerror = (event) => {
    console.log(`EventSource failed: ${event.type}`)
  }
})
</script>

<template>
  <v-layout style="height: 100%">
    <v-row justify="center" class="py-4" no-gutters style="height: 100%;">
      <v-col cols="11" xs="11" sm="11" md="11" lg="10" xl="7" xxl="6" style="height: 100%;">
        <v-card style="height: 100%">
          <v-col style="height: 100%">
            <!--消息记录区域-->
            <v-row no-gutters style="height: 90%">
              <v-col style="height: 100%;overflow-y: auto" ref="chatContainer">
                <div v-if="messages.length > 0">
                  <div v-for="n in messages">
                    <v-list-item class="text-right">
                      <template #title>
                        <v-progress-circular v-if="n.userLoading" width="2" size="13"
                                             class="mr-2"
                                             indeterminate></v-progress-circular>
                        <p class="text-body-2 rounded-lg pa-2 mb-2 message-content"
                           style="background-color: rgb(var(--v-theme-primary))">
                          {{ n.user }}</p>
                      </template>
                      <template #append>
                        <v-avatar size="small" text="You" color="primary"></v-avatar>
                      </template>
                      <template #prepend>
                        <v-avatar size="small"></v-avatar>
                      </template>
                      <template #subtitle>
                        <div class="text-disabled" style="font-size: 0.73rem;font-weight: 450">
                          <v-icon
                            icon="mdi-check-bold"
                            color="success"
                            class="mr-1"></v-icon>
                          <span>{{ n.userTime }}</span>
                        </div>

                      </template>
                    </v-list-item>
                    <v-list-item class="text-left">
                      <template #title>
                        <v-progress-circular v-if="n.aiLoading" width="2" size="13"
                                             class="mr-2"
                                             indeterminate></v-progress-circular>
                        <p v-if="n.ai" class="text-body-2 rounded-lg pa-2 mb-2 message-content text-pre-wrap"
                           style="background-color: rgb(var(--v-theme-background))">
                          {{ n.ai }}</p>
                      </template>
                      <template #prepend>
                        <v-avatar size="small" text="AI" color="brown"></v-avatar>
                      </template>
                      <template #subtitle>
                        <div class="text-disabled" style="font-size: 0.73rem;font-weight: 450">
                          <v-icon v-if="!n.aiLoading"
                                  icon="mdi-check-bold"
                                  color="success"
                                  class="mr-1"></v-icon>
                          <span>{{ n.aiTime }}</span>
                        </div>

                      </template>
                    </v-list-item>
                  </div>
                </div>
                <div v-else>
                  <v-empty-state
                    headline="Whoops, empty"
                    title="Page is empty"
                    image="https://vuetifyjs.b-cdn.net/docs/images/logos/v.png"
                  ></v-empty-state>
                </div>
              </v-col>
            </v-row>
            <!--消息发送区域-->
            <v-row no-gutters style="height: 10%" align="center">
              <v-col>
                <v-text-field v-model="currentMsg" variant="solo-filled" no-resize
                              center-affix @keydown.enter="sendMsg" placeholder="订单信息填写错误怎么办?">
                  <template #append-inner>
                    <v-btn icon="mdi-send-outline" variant="text" color="" @click="sendMsg"></v-btn>
                  </template>
                  <template #append>
                    <v-tooltip interactive>
                      <template v-slot:activator="{ props: activatorProps }">
                        <v-btn icon="mdi-information-outline" variant="text" color="" v-bind="activatorProps"></v-btn>
                      </template>
                      <div>
                        <p>
                          基于LangChain框架，结合DeepSeek大语言模型与阿里云百炼向量模型，实现了一个轻量级智能问答系统：</p>
                        <p>📚知识库：内置基于美团订单QA的知识库，涵盖31个典型订单相关问题，为用户提供针对性回答。</p>
                        <p>
                          🔍语义检索：利用内存向量存储，结合阿里云百炼向量模型进行语义向量化与检索，能够快速定位相关知识点。</p>
                        <p>🤖智能问答：由DeepSeek模型驱动，结合检索结果进行推理和生成，输出自然流畅的回答。</p>
                        <p>⚡轻量实现：采用内存向量存储，无需数据库或外部存储，部署简单、响应快速。</p>
                        <p>📝会话模式：支持即时问答，但不保留历史聊天记录，每次提问均为独立查询。</p>
                        <p>🔗LangChain集成：通过链式调用，完成“向量检索+大模型问答”的端到端流程。</p>
                      </div>
                    </v-tooltip>

                  </template>
                </v-text-field>
              </v-col>
            </v-row>
          </v-col>
        </v-card>
      </v-col>
    </v-row>
  </v-layout>
</template>

<style scoped>
.message-content {
  display: inline-block;
}
</style>
