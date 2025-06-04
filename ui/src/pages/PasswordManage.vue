<script setup>
import {ref} from "vue";

let visible = ref(false)
let dialog = ref(false)
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
  <v-row justify="center" class="py-4" no-gutters>
    <v-col cols="11" xs="11" sm="11" md="11" lg="8" xl="7" xxl="6" style="height: 100%">
      <v-row>
        <v-col cols="12">
          <v-text-field
            variant="underlined"
            prepend-inner-icon="mdi-magnify"
            placeholder="搜索密码"
          >
          </v-text-field>
        </v-col>
      </v-row>
      <v-row justify="space-around" class="align-center">
        <v-col>
          <span class="text-h5">149个网站或应用</span>
        </v-col>
        <v-col class="d-flex justify-end">
          <v-btn variant="tonal" prepend-icon="mdi-plus" @click="dialog = true">添加</v-btn>
        </v-col>
      </v-row>
      <v-row class="my-3">
        <v-expansion-panels rounded="lg" elevation="24">
          <v-expansion-panel
            selected-class="border-sm"
            v-for="i in passwords"
            :key="i.id"
            :title="i.name"
          >
            <v-expansion-panel-text>
              <v-row class="py-5">
                <v-col cols="6" class="d-flex align-center text-subtitle-1"><a :href="i.url">{{ i.url }}</a></v-col>
                <v-col cols="6">
                  <v-text-field
                    density="compact"
                    label="账号"
                    variant="outlined"
                    v-model="i.username"
                    append-icon="mdi-content-copy"
                    @click:append="copy(i.username)"
                  >
                  </v-text-field>
                </v-col>
                <v-col cols="6">
                  <v-text-field
                    density="compact"
                    label="备注"
                    variant="outlined"
                    v-model="i.name"
                    class="mt-3"
                  >
                  </v-text-field>
                </v-col>
                <v-col cols="6">
                  <v-text-field
                    density="compact"
                    label="密码"
                    :append-inner-icon="visible ? 'mdi-eye' : 'mdi-eye-off'"
                    :type="visible ? 'text' : 'password'"
                    variant="outlined"
                    v-model="i.password"
                    @click:append-inner="visible = !visible"
                    append-icon="mdi-content-copy"
                    @click:append="copy(i.password)"
                    class="mt-3"
                  >
                  </v-text-field>
                </v-col>

              </v-row>
              <v-row justify="end">
                <p class="my-2">
                  <v-btn variant="tonal" color="">更新</v-btn>
                  <v-btn variant="tonal" class="ml-5" color="error">删除</v-btn>
                </p>
              </v-row>
            </v-expansion-panel-text>
          </v-expansion-panel>
        </v-expansion-panels>
      </v-row>
    </v-col>
  </v-row>

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
  <v-dialog
    v-model="dialog"
    max-width="600"
    transition="dialog-bottom-transition"
  >
    <v-card
      prepend-icon="mdi-plus"
      title="添加密码"
    >
      <v-card-text>
        <v-row dense>
          <v-col
            cols="12"
          >
            <v-text-field
              label="备注*"
              required
              density="compact"
              prepend-inner-icon="mdi-format-title"
            ></v-text-field>
          </v-col>

          <v-col
            cols="12"
            class="mt-3"
          >
            <v-text-field
              label="网址*"
              required
              density="compact"
              prepend-inner-icon="mdi-web"
            ></v-text-field>
          </v-col>

          <v-col
            cols="12"
            class="mt-3"
          >
            <v-text-field
              label="账号*"
              required
              density="compact"
              prepend-inner-icon="mdi-account-outline"
            ></v-text-field>
          </v-col>

          <v-col
            cols="12"
            class="mt-3"
          >
            <v-text-field
              label="密码*"
              required
              density="compact"
              prepend-inner-icon="mdi-lock-outline"
            ></v-text-field>
          </v-col>

        </v-row>
      </v-card-text>

      <v-divider></v-divider>

      <v-card-actions>
        <v-btn
          color="primary"
          text="保存"
          variant="tonal"
          @click="dialog = false"
        ></v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>

</template>

<style scoped>

</style>
