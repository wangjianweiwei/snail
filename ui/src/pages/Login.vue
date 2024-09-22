<script setup>
import {useRoute, useRouter} from 'vue-router'
import {ref} from "vue";

const router = useRouter()
const route = useRoute()

const loading = ref(false)
const Login = () => {
  loading.value = true
  window.localStorage.setItem("token", "ok")
  setTimeout(() => {
    loading.value = false
    let from = route.query.from
    if (from) {
      router.push(from.toString())
    } else {
      router.push("/")
    }
  }, 2000)

}

</script>

<template>
  <v-app>
    <v-row class="d-flex justify-center">
      <v-col class="pa-12" lg="4" xl="3" sm="8" xs="10" align-self="center">
        <v-card class="pa-12" :loading="loading" rounded="lg">
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
          <form class="mt-10">
            <v-text-field
              rounded="lg"
              density="comfortable"
              label="Account"
              prepend-inner-icon="mdi-email-outline"
              variant="outlined"
            ></v-text-field>

            <v-text-field
              rounded="lg"
              density="comfortable"
              label="Password"
              prepend-inner-icon="mdi-lock-outline"
              class="mt-7"
              variant="outlined"
            ></v-text-field>
            <div class="d-flex align-center justify-space-between mt-5">
              <v-checkbox label="记住密码">

              </v-checkbox>
              <a
                class="text-caption text-decoration-none text-blue"
                href="#"
                rel="noopener noreferrer"
                target="_blank"
              >
                Forgot login password?</a>
            </div>
            <div class="mt-5">
              <v-btn block rounded="lg" @click="Login">Login</v-btn>
            </div>
            <div class="mt-7">
              <span>New on our platform? <a class="text-caption text-decoration-none text-blue"
                                            href="#"
                                            rel="noopener noreferrer"
                                            target="_blank">Create an account</a></span>
            </div>
            <div class="d-flex justify-space-between align-center mt-7">
              <v-divider></v-divider>
              <span class="mx-4">or</span>
              <v-divider></v-divider>
            </div>
            <div class="mt-7 d-flex justify-center align-center">
              <v-btn size="small" icon="mdi-wechat" class="mr-3" color="#22ac38"></v-btn>
              <v-btn size="small" icon="mdi-github" class="mr-3" color="white"></v-btn>
              <v-btn size="small" icon="mdi-google" class="mr-3" color="#EA4335"></v-btn>
              <v-btn size="small" icon="mdi-facebook" class="mr-3" color="#497ce2"></v-btn>
              <v-btn size="small" icon="mdi-twitter" color="#1da1f2"></v-btn>
            </div>
          </form>
        </v-card>
      </v-col>
    </v-row>

  </v-app>

</template>

<style scoped>

</style>
