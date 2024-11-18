<script setup>
import {useRoute, useRouter} from 'vue-router'
import {ref, onMounted} from "vue";
import {loginApi} from '@/services'

const router = useRouter()
const route = useRoute()

const loading = ref(false)
const email = ref(null)
const otp_code = ref(null)

const Login = async () => {
  loading.value = true
  let data = await loginApi(email.value, otp_code.value)
  console.log(data, "//////")
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
      <v-col class="pa-12" lg="4" xl="3" sm="8" xs="10" align-self="center">
        <v-card class="pa-5" :loading="loading" rounded="lg">
          <template v-slot:loader="{ isActive }">
            <v-progress-linear
              :active="isActive"
              color="primary"
              height="4"
              indeterminate
            ></v-progress-linear>
          </template>
          <p class="text-h5 font-weight-bold">Welcome to
            <span class="text-decoration-underline" style="color: #696CFF">me.discuss.pub</span>👋🏻</p>
          <p class="text-body-2 text-disabled">Please sign-in to your account and start the adventure</p>
          <div class="mt-12">
            <v-text-field density="compact" variant="outlined" label="邮箱" v-model="email"></v-text-field>
          </div>
          <div class="mt-3">
            <v-otp-input focus-all :length="6" v-model="otp_code"></v-otp-input>
          </div>
          <div class="mt-3">
            <v-btn block text="登陆" @click="Login"></v-btn>
          </div>
          <v-divider class="my-7"></v-divider>
          <div class="mt-7">
            <span>New on our platform? </span><a class="text-caption text-decoration-none text-blue"
                                                 href="/register"
                                                 rel="noopener noreferrer"
                                                 target="_blank">Create an account</a>
          </div>
        </v-card>
      </v-col>
    </v-row>
  </v-app>

</template>

<style scoped>

</style>
