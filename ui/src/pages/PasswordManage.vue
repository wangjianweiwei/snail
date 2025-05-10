<script setup>
import {ref} from "vue";

let visible = ref(false)
const snackbar = ref(false)
let passwords = ref([])

for (let i = 0; i < 35; i++) {
  passwords.value.push(
    {
      id: i,
      name: "xxx2",
      url: "http://localhost:8080",
      username: "zhangsan2",
      password: '223455'
    }
  )
}

function copy(text) {
  navigator.clipboard.writeText(text).then(function () {
    snackbar.value = true
  })
}
</script>

<template>
  <v-row justify="center" style="height: 100%;overflow-y: scroll">
    <v-col cols="6">
      <v-card class="mt-5" border>
        <v-row justify="space-between" class="align-center">
          <v-col>
            <span class="text-h5">149个网站或应用</span>
            <span> 添加</span>
          </v-col>
          <v-col>
            <v-text-field
              variant="underlined"
              prepend-inner-icon="mdi-magnify"
              placeholder="搜索密码"
            >
            </v-text-field>
          </v-col>
        </v-row>

        <v-row>
          <v-expansion-panels focusable>
            <v-expansion-panel
              v-for="i in passwords"
              :key="i.id"
              :title="i.name"
            >
              <v-expansion-panel-text>
                <v-row>
                  <v-col cols="4"><a :href="i.url">{{ i.url }}</a></v-col>
                  <v-col cols="8">
                    <v-text-field
                      label="账号"
                      variant="outlined"
                      v-model="i.username"
                    >
                      <template v-slot:append>
                        <v-btn
                          icon="mdi-content-copy"
                          variant="text"
                          color=""
                          @click="copy(i.username)">
                        </v-btn>
                      </template>
                    </v-text-field>
                    <v-text-field
                      label="密码"
                      :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
                      :type="visible ? 'text' : 'password'"
                      variant="outlined"
                      v-model="i.password"
                      @click:append-inner="visible = !visible"
                      class="mt-3"
                    >
                      <template v-slot:append>
                        <v-btn
                          icon="mdi-content-copy"
                          variant="text"
                          color=""
                          @click="copy(i.password)">
                        </v-btn>
                      </template>
                    </v-text-field>
                    <p class="mt-3">
                      <v-btn variant="text" color="">更新</v-btn>
                      <v-btn variant="text" class="ml-5" color="error">删除</v-btn>
                    </p>
                  </v-col>
                </v-row>
              </v-expansion-panel-text>
            </v-expansion-panel>
          </v-expansion-panels>
        </v-row>
      </v-card>
    </v-col>
    <v-snackbar
      v-model="snackbar"
      color="grey-darken-3"
      timeout="700"
      location="top right"
      variant="elevated"
      text="snackbarText"
    >
      <template v-slot:text>
        <span class="mdi mdi-check-bold mr-3"></span>
        <span>复制成功</span>
      </template>
    </v-snackbar>
  </v-row>
</template>

<style scoped>

</style>
