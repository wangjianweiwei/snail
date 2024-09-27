<script setup>
import {useRoute, useRouter} from 'vue-router'
import {routes} from "@/plugins/router";
import {hexToRgb} from "@/@layouts/utils";
import {useTheme} from 'vuetify'

const {global} = useTheme()


const route = useRoute()

</script>


<template>
  <v-app id="inspire" :style="`--v-global-theme-primary: ${hexToRgb(global.current.value.colors.primary)}`">
    <v-app-bar class="border-b-sm">
      <v-container fluid class="pa-12">
        <div class="d-flex justify-space-between">
          <div style="display: flex;align-items: center">
            <v-btn style="text-transform: none" prepend-icon="$vuetify" variant="plain" color="" size="x-large"><h4>By
              Vuetifyjs</h4></v-btn>
          </div>

          <div>
            <v-btn icon="mdi-magnify" variant="text" color=""></v-btn>
            <v-btn icon="mdi-weather-night" variant="text" color=""></v-btn>
            <v-btn icon="mdi-bell-outline" variant="text" color=""></v-btn>
            <v-menu location="bottom">
              <template v-slot:activator="{ props }">
                <v-avatar
                  class="ml-2"
                  v-bind="props"
                  image="https://demos.themeselection.com/sneat-vuetify-vuejs-admin-template/demo-1/assets/avatar-1-DL1ARROH.png"
                >
                </v-avatar>
              </template>
              <v-list width="230" density="compact" rounded border="sm">
                <v-list-item
                  title="asd"
                  subtitle="admin"
                  prepend-avatar="https://demos.themeselection.com/sneat-vuetify-vuejs-admin-template/demo-1/assets/avatar-1-DL1ARROH.png">
                </v-list-item>
                <v-divider class="my-2"></v-divider>
                <v-list-item
                  key="Profile"
                  value="Profile"
                  to="Profile">
                  <template #default>
                    <p class="text-sm-body-2">
                      <v-icon icon="mdi-account-outline"></v-icon>
                      <span class="ml-2 text-lg-body-1">&nbsp;&nbsp;Profile</span>
                    </p>
                  </template>
                </v-list-item>
                <v-list-item
                  key="child.meta.subMenu"
                  value="child.meta.subMenu"
                  to="child.meta.fullPath">
                  <template #default>
                    <p class="text-sm-body-2">
                      <v-icon icon="mdi-cog-outline"></v-icon>
                      <span class="ml-2 text-lg-body-1">&nbsp;&nbsp;Settings</span>
                    </p>
                  </template>
                </v-list-item>
                <v-divider class="my-2"></v-divider>
                <v-list-item
                  key="Logout"
                  value="Logout"
                  to="Logout">
                  <template #default>
                    <p class="text-sm-body-2">
                      <v-icon icon="mdi-logout"></v-icon>
                      <span class="ml-2 text-lg-body-1">&nbsp;&nbsp;Logout</span>
                    </p>
                  </template>
                </v-list-item>
              </v-list>
            </v-menu>
          </div>
        </div>
      </v-container>
    </v-app-bar>
    <v-app-bar class="border-b-sm">
      <v-container fluid class="pa-12">
        <v-menu
          offset="13"
          open-on-hover
          open-delay="10"
          close-delay="10"
          transition="scroll-y-reverse-transition"
          v-for="menu in routes[0]['children']"
        >
          <template v-slot:activator="{ props }">
            <v-btn
              style="font-weight: normal"
              :variant="route.meta.parentMenu === menu.meta.parentMenu ?'flat': 'text'"
              :color="route.meta.parentMenu === menu.meta.parentMenu ?'#696CFF': ''"
              class="text-none text-subtitle-1 mr-2"
              :prepend-icon="menu.meta.parentMenuIcon"
              append-icon="mdi-chevron-down"
              v-bind="props"
            >
              {{ menu.meta.parentMenu }}
            </v-btn>
          </template>
          <v-list density="compact" border="sm" rounded width="200px">
            <v-list-item
              v-for="child in menu.children.filter(n => {return n.meta?.subMenu})"
              :key="child.meta.subMenu"
              :value="child.meta.subMenu"
              :to="child.meta.fullPath">
              <template #default>
                <p class="text-sm-body-2">
                  <v-icon :icon="child.meta.subMenuIcon"></v-icon>
                  <span class="ml-2 text-lg-body-1">&nbsp;&nbsp;{{ child.meta.subMenu }}</span>
                </p>
              </template>
            </v-list-item>
          </v-list>
        </v-menu>
      </v-container>
    </v-app-bar>

    <v-main scrollable>
      <v-slide-y-reverse-transition>
        <router-view></router-view>
      </v-slide-y-reverse-transition>
    </v-main>


    <!--    <v-footer app color="#232332" class="text-center d-flex justify-center text-green py-1 px-12 text-grey-lighten-1">-->
    <!--      <div class="text-sm-body-2">-->
    <!--        {{ new Date().getFullYear() }} — <span>Vuetify</span><span> 京公网安备11000002000001号</span>-->
    <!--      </div>-->
    <!--    </v-footer>-->
  </v-app>


</template>
<style scoped lang="scss">

</style>
