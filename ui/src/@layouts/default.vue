<script setup>
import {useRoute, useRouter} from 'vue-router'
import {routes} from "@/plugins/router";
import {useTheme} from 'vuetify'
import {ref, onMounted, reactive} from "vue";
import {useI18n} from "vue-i18n"
import {componentStyleConfig} from "@/plugins/vuetify/defaults"
import {primaryColor} from "@/plugins/vuetify/theme";

const {t, locale} = useI18n()
const theme = useTheme()
const drawer = ref(false)
const configDrawer = ref(false)
const authState = localStorage.getItem("token")
const route = useRoute()
const router = useRouter()
const currentDark = ref(true)
const language = ref(["zh"])
const defaultOpenMenus = ref([])

onMounted(() => {
  routes[0]['children'].forEach((e) => {
    console.log(e.path)
    defaultOpenMenus.value.push(e.path)
  })
})

async function logout() {
  localStorage.removeItem("token")
  await router.push("/posts/list")
}

function toggleTheme(e) {
  const isDark = theme.global.current.value.dark;
  console.log(theme)

  // 手动同步 `<html>` 的 dark 类
  if (isDark) {
    document.documentElement.classList.remove('dark');
  } else {
    document.documentElement.classList.add('dark');
  }
  const transition = document.startViewTransition(() => {
    theme.global.name.value = theme.global.current.value.dark ? 'light' : 'dark'
    currentDark.value = theme.global.name.value === "dark"
  })
  transition.ready.then(() => {
    // 由于我们要从鼠标点击的位置开始做动画，所以我们需要先获取到鼠标的位置
    const {clientX, clientY} = e
    console.log(clientX, clientY)

    // 计算半径，以鼠标点击的位置为圆心，到四个角的距离中最大的那个作为半径
    const radius = Math.hypot(
      Math.max(clientX, innerWidth - clientX),
      Math.max(clientY, innerHeight - clientY)
    )
    const clipPath = [
      `circle(0% at ${clientX}px ${clientY}px)`,
      `circle(${radius}px at ${clientX}px ${clientY}px)`
    ]
    const isDark = theme.global.name.value === "dark"
    console.log("isDark", isDark, theme.global.name.value)
    // 自定义动画
    document.documentElement.animate(
      {
        // 如果要切换到暗色主题，我们在过渡的时候从半径 100% 的圆开始，到 0% 的圆结束
        clipPath: isDark ? clipPath.reverse() : clipPath
      },
      {
        duration: 500,
        // 如果要切换到暗色主题，我们应该裁剪 view-transition-old(root) 的内容
        pseudoElement: isDark
          ? '::view-transition-old(root)'
          : '::view-transition-new(root)'
      }
    )
  })

}

function translate(value) {
  locale.value = value[0]
}

</script>


<template>
  <v-app>
    <v-app-bar flat class="border-b px-3">
      <v-app-bar-nav-icon
        class="d-sm-flex d-md-none"
        @click="drawer = !drawer"
      ></v-app-bar-nav-icon>
      <v-app-bar-title class="d-none d-md-flex">
        <h2 class="text-disabled">👋</h2>
      </v-app-bar-title>
      <template v-slot:append>
        <div class="d-flex align-center ga-3">
          <div class="d-none d-md-flex ga-2">
            <v-menu
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
                  :text="t(menu.meta.parentMenu)"
                >

                </v-btn>
              </template>
              <v-list v-if="menu.meta.hasSub" density="compact" width="200px">
                <v-list-item
                  v-for="child in menu.children.filter(n => {return n.meta?.subMenu})"
                  class="mx-2 my-1"
                  rounded
                  :key="child.meta.subMenu"
                  :value="child.meta.subMenu"
                  :to="child.meta.fullPath">
                  <template #default>
                    <p class="d-flex justify-space-between align-center">
                      <span class="text-body-2">{{ t(child.meta.subMenu) }}</span>
                      <v-icon :icon="child.meta.subMenuIcon"></v-icon>
                    </p>
                  </template>
                </v-list-item>
              </v-list>
            </v-menu>
          </div>
          <div>
            <!--            <v-btn icon="mdi-magnify" variant="text" color=""></v-btn>-->
            <!--            <v-btn icon="mdi-bell-outline" variant="text" color=""></v-btn>-->
            <v-btn v-if="currentDark" icon="mdi-weather-night" variant="text" color="" @click="toggleTheme"></v-btn>
            <v-btn v-else icon="mdi-white-balance-sunny" variant="text" color="" @click="toggleTheme"></v-btn>
            <v-menu open-on-hover>
              <template v-slot:activator="{ props }">
                <v-btn
                  color=""
                  variant="text"
                  icon="mdi-translate"
                  v-bind="props"
                >
                </v-btn>
              </template>
              <v-list selectable density="compact" v-model:selected="language" @update:selected="translate">
                <v-list-item class="mx-2 my-1" value="zh" rounded>
                  <template #default>
                    <span class="text-body-2">中文</span>
                  </template>
                </v-list-item>
                <v-list-item class="mx-2 my-1" value="en" rounded>
                  <template #default>
                    <span class="text-body-2">English</span>
                  </template>
                </v-list-item>
              </v-list>
            </v-menu>
            <v-btn icon="mdi-cog-outline" color="" @click="configDrawer = true"></v-btn>
          </div>
          <div>
            <v-menu v-if="authState" location="bottom">
              <template v-slot:activator="{ props }">
                <v-avatar
                  color="primary"
                  v-bind="props"
                >
                  <span class="text-h6">will</span>
                </v-avatar>
              </template>
              <v-list width="200" density="compact">
                <v-list-item
                  title="admin"
                  subtitle="will">
                  <template #prepend>
                    <v-avatar
                      color="primary"
                    >
                      <span class="text-h6">will</span>
                    </v-avatar>
                  </template>
                </v-list-item>
                <v-divider class="my-2"></v-divider>
                <v-list-item
                  rounded
                  class="mx-2 my-1"
                  key="Profile"
                  value="Profile">
                  <template #default>
                    <p class="d-flex justify-start align-center">
                      <v-icon icon="mdi-account-outline"></v-icon>
                      <span class="text-body-2 ml-4">个人中心</span>
                    </p>
                  </template>
                </v-list-item>
                <v-list-item
                  rounded
                  class="mx-2 my-1">
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
      </template>
    </v-app-bar>


    <v-main scrollable>
      <router-view v-slot="{ Component }">
        <v-slide-y-reverse-transition>
          <component :is="Component"/>
        </v-slide-y-reverse-transition>

      </router-view>

    </v-main>
    <v-navigation-drawer v-model="drawer" temporary elevation="0" class="d-sm-flex d-md-none pa-2">
      <template v-slot:prepend>
        <div class="d-flex justify-center">
          <h2 class="text-disabled">👋</h2>
        </div>
      </template>
      <v-list density="compact" nav v-model:opened="defaultOpenMenus">
        <div v-for="menu in routes[0]?.children">
          <v-list-group v-if="menu.meta.hasSub" :value="menu.path">
            <template v-slot:activator="{ props }">
              <v-list-item
                v-bind="props"
                :title="t(menu.meta.parentMenu)"
              ></v-list-item>
            </template>
            <v-list-item
              rounded="lg"
              v-for="subMenu in menu.children"
              :key="subMenu.meta.fullPath"
              :to="subMenu.meta.fullPath"
              :append-icon="subMenu.meta.subMenuIcon"
            >
              <v-list-item-title>{{ t(subMenu.meta.subMenu) }}</v-list-item-title>
            </v-list-item>
          </v-list-group>
          <v-list-item v-else
                       rounded="lg"
                       :to="menu.meta.fullPath"
                       :title="t(menu.meta.parentMenu)"
                       :append-icon="menu.meta.parentMenuIcon">
          </v-list-item>
        </div>

      </v-list>
    </v-navigation-drawer>
    <v-navigation-drawer width="320" v-model="configDrawer" location="right" temporary elevation="0">
      <div class="pa-3">
        <p class="text-h5">主题定制</p>
        <p class="text-body-2 text-disabled">实时自定义和预览</p>
      </div>
      <v-divider></v-divider>
      <div class="px-3">
        <h3 class="text-h6 my-6">边框</h3>
        <v-radio-group v-model="componentStyleConfig.border" density="default">
          <v-radio label="不显示" :value="false"></v-radio>
          <v-radio label="显示" :value="true"></v-radio>
        </v-radio-group>
        <h3 class="text-h6 my-6">圆角</h3>
        <v-radio-group v-model="componentStyleConfig.rounded" density="default">
          <v-radio label="取消" :value="false"></v-radio>
          <v-radio label="lg" value="lg"></v-radio>
          <v-radio label="xl" value="xl"></v-radio>
          <v-radio label="shaped" value="shaped"></v-radio>
        </v-radio-group>
        <h3 class="text-h6 my-6">主题色</h3>
        <v-radio-group v-model="primaryColor" density="default">
          <v-radio label="#696CFF" value="#696CFF">
            <template v-slot:label>
              <strong style="color: #696CFF">#696CFF</strong>
            </template>
          </v-radio>
          <v-radio label="#008889" value="#008889" base-color="#008889">
            <template v-slot:label>
              <strong style="color: #008889">#008889</strong>
            </template>
          </v-radio>
          <v-radio label="#FFA823" value="#FFA823" base-color="#FFA823">
            <template v-slot:label>
              <strong style="color: #FFA823">#FFA823</strong>
            </template>
          </v-radio>
          <v-radio label="#FF434A" value="#FF434A" base-color="#FF434A">
            <template v-slot:label>
              <strong style="color: #FF434A">#FF434A</strong>
            </template>
          </v-radio>
          <v-radio label="#00ABFC" value="#00ABFC" base-color="#00ABFC">
            <template v-slot:label>
              <strong style="color: #00ABFC">#00ABFC</strong>
            </template>
          </v-radio>
        </v-radio-group>
        <v-color-input variant="underlined" class="ml-2 mt-1" density="default" v-model="primaryColor"></v-color-input>
        <h3 class="text-h6 my-6">按钮</h3>
        <v-radio-group v-model="componentStyleConfig.btnVariant" density="default">
          <v-radio value="elevated">
            <template v-slot:label>
              <v-btn variant="elevated" text="example"></v-btn>
            </template>
          </v-radio>
          <v-radio value="flat" class="pt-2">
            <template v-slot:label>
              <v-btn variant="flat" text="example"></v-btn>
            </template>
          </v-radio>
          <v-radio value="tonal" class="pt-2">
            <template v-slot:label>
              <v-btn variant="tonal" text="example"></v-btn>
            </template>
          </v-radio>
          <v-radio value="outlined" class="pt-2">
            <template v-slot:label>
              <v-btn variant="outlined" text="example"></v-btn>
            </template>
          </v-radio>
          <v-radio value="text" class="pt-2">
            <template v-slot:label>
              <v-btn variant="text" text="example"></v-btn>
            </template>
          </v-radio>
          <v-radio value="plain" class="pt-2">
            <template v-slot:label>
              <v-btn variant="plain" text="example"></v-btn>
            </template>
          </v-radio>

        </v-radio-group>
        <h3 class="text-h6 my-6">阴影</h3>
        <v-slider
          v-model="componentStyleConfig.elevation"
          show-ticks="always"
          step="2"
          max="24"
        ></v-slider>
      </div>

    </v-navigation-drawer>
  </v-app>


</template>
<style>
::view-transition-new(root),
::view-transition-old(root) {
  animation: none !important;;
}

.dark::view-transition-old(root) {
  z-index: 1 !important;
}
</style>
