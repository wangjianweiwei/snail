<script setup>
import {useRoute, useRouter} from 'vue-router'
import {ref, onMounted} from "vue";
import {loginApi} from '@/services'

const router = useRouter()
const route = useRoute()


const loading = ref(false)
const snackbar = ref(false)

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

const noSupport = () => {
  snackbar.value = true
}

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

const GithubLogin = () => {
  window.location = "https://github.com/login/oauth/authorize?client_id=17f2d31fca5f88282646&redirect_uri=http://localhost:3000/login&socpe=user"
  // router.push("https://github.com/login/oauth/authorize?client_id=17f2d31fca5f88282646&redirect_uri=http://127.0.0.1:3000/login")
}

const loginMethods = [
  {
    method: "Wechat",
    icon: "mdi-wechat",
    click: noSupport,
    color: "#22ac38"
  },
  {
    method: "github",
    icon: "mdi-github",
    click: GithubLogin,
    color: "white"
  },
  {
    method: "google",
    icon: "mdi-google",
    click: noSupport,
    color: "#EA4335"
  },
  {
    method: "facebook",
    icon: "mdi-facebook",
    click: noSupport,
    color: "#497ce2"
  },
  {
    method: "twitter",
    icon: "mdi-twitter",
    click: noSupport,
    color: "#1da1f2"
  }
]
</script>

<template>
  <v-app>
    <v-row no-gutters class="d-flex justify-center">
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
          <div class="mt-7">
            <span>New on our platform? </span>
          </div>
          <v-divider class="my-3"></v-divider>
          <div class="mt-7 d-flex justify-center align-center">
            <v-btn v-for="n in loginMethods" :icon="n.icon" class="mr-3"
                   :color="n.color"
                   @click="n.click"></v-btn>
          </div>
        </v-card>
      </v-col>
    </v-row>
    <v-snackbar
      v-model="snackbar"
      offset="100"
      timeout="2000"
      timer
      transition="scroll-x-reverse-transition"
      multi-line
      rounded="lg"
      location="top right"
      text="暂不支持 🤓"
      close-on-content-click
    >
      <template v-slot:actions>
        <v-btn
          color="blue"
          variant="text"
          @click="snackbar = false"
        >
          Close
        </v-btn>
      </template>
    </v-snackbar>
  </v-app>

</template>

<style scoped>

</style>
