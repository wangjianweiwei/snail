<script setup>
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
</script>

<template>
  <div style="height: 100%" class="pa-10">
    <v-row justify="center" no-gutters style="height: 100%">
      <v-col lg="12" xl="8">
        <v-card border rounded="lg" style="height: 100%" class="pa-5 mx-10">
          <v-row style="height: 8%" class="border">
            <v-col cols="3">
              <v-sheet>
                头像
              </v-sheet>
            </v-col>
            <v-col cols="9">
              <v-sheet>
                <p>对话工具栏</p>
              </v-sheet>
            </v-col>
          </v-row>
          <v-row style="height: 92%" class="border">
            <v-col cols="3" style="height: 100%;overflow-y: scroll">
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
              <p>好友列表</p>
            </v-col>
            <v-col cols="9" style="height: 100%">
              <v-row style="height: 90%;overflow-y: scroll" class="border">
                <v-col class="pa-3">
                  <v-sheet>
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
                  </v-sheet>
                </v-col>
              </v-row>
              <v-row style="height: 10%" class="border">
                <v-col>
                  <v-sheet>
                    <v-textarea no-resize center-affix rows="3">
                      <template #append-inner>
                        <v-icon icon="$vuetify"></v-icon>
                        <v-btn>发送</v-btn>
                      </template>
                    </v-textarea>
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
</style>
