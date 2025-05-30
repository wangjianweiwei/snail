<script setup>
import {useRoute, useRouter} from 'vue-router'
import {ref, onMounted} from "vue";
import {createOtpQrcodeApi, registerApi} from '@/services'

const router = useRouter()
const route = useRoute()


const loading = ref(false)
const qrcode = ref(null)
const secret = ref(null)
const email = ref("")

onMounted(() => {
  let code = route.query.code
  console.log("code", code)
  if (code) {
    loading.value = true
    loginApi(code).then((response) => {
      console.log(response)
      console.log(data, "loginApi")
      loading.value = false
    })


  }

})

async function createOtpQrcode() {
  loading.value = true
  let data = await createOtpQrcodeApi(email.value)
  qrcode.value = data.qrcode
  secret.value = data.secret
  loading.value = false
}

const register = async () => {
  loading.value = true
  await registerApi(email.value, secret.value)
  loading.value = false
  await router.push("/")

}

</script>

<template>
  <v-app>
    <v-row no-gutters class="d-flex justify-center">
      <v-col class="pa-10" lg="4" xl="3" sm="8" xs="10" align-self="center">
        <v-card class="pa-5" :loading="loading">
          <template v-slot:loader="{ isActive }">
            <v-progress-linear
              :active="isActive"
              color="primary"
              height="4"
              indeterminate
            ></v-progress-linear>
          </template>
          <p class="text-h5 font-weight-bold">Welcome to
            <span class="text-decoration-underline" style="color: #696CFF">me.discuss.pub </span>👋🏻</p>
          <p class="text-body-2 text-disabled">Please sign-in to your account and start the adventure</p>
          <v-divider class="mt-4 mb-8"></v-divider>
          <div>
            <v-text-field :disabled="qrcode" density="compact" variant="outlined" label="输入一个用户名开始初始化😎"
                          v-model="email"></v-text-field>
          </div>
          <div class="my-8" v-if="!qrcode">
            <v-btn text="确认" block @click="createOtpQrcode"></v-btn>
          </div>
          <v-row class="mt-8" no-gutters v-else>
            <v-col cols="6">
              <p class="text-body-2">扫描二维码</p>
              <v-img
                :width="150"
                aspect-ratio="16/9"
                cover
                class="mt-2"
                rounded
                :src="`data:image/png;base64,${qrcode}`"
              ></v-img>
            </v-col>
            <v-col cols="6" style="font-size: 0.75rem">
              <p>1. 请使用您手机中的认证应用（如 Google Authenticator、Microsoft Authenticator 等）扫描左侧二维码。</p>
              <p class="mt-1">2. 扫描成功后，认证应用将生成一个动态验证码。</p>
              <p class="mt-1">3. 输入动态验证码以完成注册。</p>
              <p class="text-disabled mt-3">提示：请妥善保存此二维码。如果需要在新设备上重新设置验证，可以再次扫描。</p>
            </v-col>
            <v-col cols="12" class="mt-5">
              <v-btn text="初始化" block @click="register"></v-btn>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
  </v-app>

</template>

<style scoped>

</style>
