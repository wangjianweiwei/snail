<script setup>
import {useRoute, useRouter} from 'vue-router'
import {routes} from "@/plugins/router";
import {hexToRgb} from "@/@layouts/utils";
import {useTheme} from 'vuetify'
import {ref} from "vue";

const {global} = useTheme()
const drawer = ref(false)
const authState = localStorage.getItem("token")
const route = useRoute()
const router = useRouter()

async function logout() {
  localStorage.removeItem("token")
  await router.push("/posts/list")
}

</script>


<template>
  <v-app>
    <v-app-bar class="border-b-sm">
      <template v-slot:prepend>
        <v-btn style="text-transform: none" variant="plain" color="" size="x-large">
          <h1 style="display: inline">👋</h1><h4>&nbsp;me.discuss.pub</h4>
        </v-btn>
      </template>
      <template v-slot:append>
        <v-col class="d-none d-md-flex" cols="auto">
          <div class="d-flex align-center">
            <div class="mr-6">
              <v-menu
                offset="13"
                open-on-hover
                open-delay="7"
                close-delay="10"
                transition="scale-transition"
                v-for="menu in routes[0]['children']"
              >
                <template v-slot:activator="{ props }">
                  <v-btn
                    style="font-weight: normal"
                    :variant="route.meta.parentMenu === menu.meta.parentMenu ?'flat': 'text'"
                    :color="route.meta.parentMenu === menu.meta.parentMenu ?'primary': ''"
                    :active="false"
                    class="text-none text-subtitle-1 mr-2"
                    :prepend-icon="menu.meta.parentMenuIcon"
                    :append-icon="menu.meta.hasSub ? 'mdi-chevron-down': ''"
                    v-bind="props"
                    :to="menu.meta.fullPath"
                    :text="menu.meta.parentMenu"
                  >

                  </v-btn>
                </template>
                <v-list v-if="menu.meta.hasSub" density="compact" border="sm" rounded width="200px">
                  <v-list-item
                    v-for="child in menu.children.filter(n => {return n.meta?.subMenu})"
                    class="mx-2 my-1"
                    rounded
                    :key="child.meta.subMenu"
                    :value="child.meta.subMenu"
                    :to="child.meta.fullPath">
                    <template #default>
                      <p class="d-flex justify-space-between align-center">
                        <span class="text-body-2">{{ child.meta.subMenu }}</span>
                        <v-icon :icon="child.meta.subMenuIcon"></v-icon>
                      </p>
                    </template>
                  </v-list-item>
                </v-list>
              </v-menu>
            </div>
            <div class="mr-6">
              <v-divider vertical></v-divider>
              <v-btn icon="mdi-magnify" variant="text" color=""></v-btn>
              <v-btn icon="mdi-weather-night" variant="text" color=""></v-btn>
              <v-btn icon="mdi-bell-outline" variant="text" color=""></v-btn>
            </div>
            <div class="mr-6">
              <v-menu v-if="authState" location="bottom">
                <template v-slot:activator="{ props }">
                  <v-avatar
                    color="primary"
                    class="ml-2"
                    v-bind="props"
                  >
                    <span class="text-h6">wangjianwei</span>
                  </v-avatar>
                </template>
                <v-list width="230" density="comfortable" border="sm" rounded>
                  <v-list-item
                    title="admin"
                    subtitle="wangjianwei">
                    <template #prepend>
                      <v-avatar
                        color="primary"
                        class="ml-2"
                      >
                        <span class="text-h6">wangjianwei</span>
                      </v-avatar>
                    </template>
                  </v-list-item>
                  <v-divider class="my-2"></v-divider>
                  <v-list-item
                    rounded
                    class="mx-2 my-1"
                    key="Profile"
                    value="Profile"
                    to="Profile">
                    <template #default>
                      <p class="d-flex justify-start align-center">
                        <v-icon icon="mdi-account-outline"></v-icon>
                        <span class="text-body-2 ml-4">个人中心</span>
                      </p>
                    </template>
                  </v-list-item>
                  <v-list-item
                    rounded
                    class="mx-2 my-1"
                    key="child.meta.subMenu"
                    value="child.meta.subMenu"
                    to="child.meta.fullPath">
                    <template #default>
                      <p class="d-flex justify-start align-center">
                        <v-icon icon="mdi-cog-outline"></v-icon>
                        <span class="text-body-2 ml-4">设置</span>
                      </p>
                    </template>
                  </v-list-item>
                  <v-list-item
                    rounded
                    class="mx-2 my-1"
                    key="Logout"
                    value="Logout"
                    @click="logout">
                    <template #default>
                      <p class="d-flex justify-start align-center">
                        <v-icon icon="mdi-logout"></v-icon>
                        <span class="text-body-2 ml-4">退出登录</span>
                      </p>
                    </template>
                  </v-list-item>
                </v-list>
              </v-menu>
              <v-btn v-else text="登录" append-icon="mdi-login" to="/login"></v-btn>
            </div>
          </div>
        </v-col>
        <v-app-bar-nav-icon
          class="d-sm-none"
          @click="drawer = !drawer"
        ></v-app-bar-nav-icon>
      </template>
    </v-app-bar>
    <v-navigation-drawer v-model="drawer" temporary class="d-sm-none">
      <v-list density="compact">
        <div v-for="menu in routes[0]?.children">
          <v-list-group v-if="menu.meta.hasSub">
            <template v-slot:activator="{ props }">
              <v-list-item
                v-bind="props"
                :title="menu.meta.parentMenu"
              ></v-list-item>
            </template>
            <v-list-item
              v-for="subMenu in menu.children"
              :key="subMenu.meta.fullPath"
              :to="subMenu.meta.fullPath"
              :append-icon="subMenu.meta.subMenuIcon"
            >
              <v-list-item-title>{{ subMenu.meta.subMenu }}</v-list-item-title>
            </v-list-item>
          </v-list-group>
          <v-list-item v-else
                       :to="menu.meta.fullPath"
                       :title="menu.meta.parentMenu"
                       :append-icon="menu.meta.parentMenuIcon"
          >
          </v-list-item>
        </div>

      </v-list>
    </v-navigation-drawer>


    <v-main scrollable>
      <v-slide-y-reverse-transition>
        <router-view></router-view>
      </v-slide-y-reverse-transition>
    </v-main>

  </v-app>


</template>
<style scoped lang="scss">

</style>
