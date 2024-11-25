<script setup>
import {useRoute, useRouter} from 'vue-router'
import {ref, provide} from "vue";
import {loginApi} from '@/services'

const router = useRouter()
const route = useRoute()

const loading = ref(false)
const email = ref(null)
const otp_code = ref(null)
const clickConfirm = ref(false)

const Login = async () => {
  loading.value = true
  let data = await loginApi(email.value, otp_code.value)
  console.log(data, "//////")
  provide('authState', true);
  window.localStorage.setItem("token", data.token)
  loading.value = false
  let from = route.query.from
  if (from) {
    await router.push(from.toString())
  } else {
    await router.push("/")
  }
}

</script>

<template>
  <v-app>
    <v-row no-gutters class="d-flex justify-center">
      <v-col class="pa-10" lg="4" xl="3" sm="8" xs="10" align-self="center">
        <v-card class="pa-5" :loading="loading" rounded="lg">
          <template v-slot:loader="{ isActive }">
            <v-progress-linear
              :active="isActive"
              color="primary"
              height="4"
              indeterminate
            ></v-progress-linear>
          </template>
          <div>
            <p class="text-h5 font-weight-bold">Welcome to
              <span class="text-decoration-underline" style="color: #696CFF">me.discuss.pub </span>👋🏻</p>
            <p class="text-body-2 text-disabled">Please sign-in to your account and start the adventure</p>
          </div>

          <v-divider class="mt-4 mb-8"></v-divider>

          <div v-if="!clickConfirm">
            <v-text-field density="compact" variant="outlined" label="输入邮箱进行登录😎"
                          v-model="email"></v-text-field>
            <v-btn class="mt-8" block text="确认" @click="clickConfirm = true"></v-btn>
          </div>
          <div v-else>
            <div class="text-body-2">
              <p class="font-weight-bold mb-2">确认你的身份</p>
              <p>
                <span>从你的密码管理APP中查看 <span class="font-weight-bold text-primary">{{ email }}</span> 的登录验证码</span>
              </p>
            </div>
            <v-otp-input max-width="100%" class="mt-2" focus-all :length="6"
                         v-model="otp_code"></v-otp-input>
            <v-btn class="mt-8" block text="登陆" @click="Login"></v-btn>
          </div>
        </v-card>
      </v-col>
    </v-row>
  </v-app>

</template>

<style scoped>
.v-otp-input__content {
  padding: 0.5rem 0 !important;
}
</style>
