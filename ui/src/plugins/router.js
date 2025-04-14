import {createWebHistory, createRouter} from 'vue-router'


const routes = [
  {
    path: '/',
    redirect: '/posts/list',
    component: () => import('../@layouts/default.vue'),
    children: [
      {
        path: '/posts',
        redirect: '/posts/list',
        meta: {parentMenu: "博客", parentMenuIcon: "mdi-post-outline", fullPath: "/posts", hasSub: false},
        children: [
          {
            path: 'list',
            meta: {requiresAuth: false},
            component: () => import('../pages/Posts.vue'),
          },
          {
            path: 'category',
            component: () => import('../pages/PostCategory.vue'),
          },
          {
            path: 'tag',
            component: () => import('../pages/PostTag.vue'),
          },
          {
            path: 'timeline',
            component: () => import('../pages/PostTimeline.vue'),
          },
          {
            path: 'compose/:id',
            meta: {requiresAuth: true},
            component: () => import('../pages/PostsEditor.vue'),
          },
          {
            path: 'preview/:id',
            meta: {requiresAuth: false},
            component: () => import('../pages/PostsPreview.vue'),
          },
        ]
      },
      {
        path: '/dashboards',
        redirect: '/dashboards/profile',
        meta: {parentMenu: "首页", parentMenuIcon: "mdi-home", hasSub: true},
        children: [
          {
            path: "profile",
            component: () => import('../pages/UserProfile.vue'),
            meta: {
              subMenu: "关于我",
              subMenuIcon: "mdi-account-outline",
              fullPath: "/dashboards/profile",
              requiresAuth: true
            }
          },
          {
            path: "settings",
            component: () => import('../pages/Settings.vue'),
            meta: {subMenu: "设置", subMenuIcon: "mdi-cogs", fullPath: "/dashboards/settings"}
          }
        ]
      },
      {
        path: '/apps',
        meta: {parentMenu: "应用", parentMenuIcon: "mdi-apps", hasSub: true},
        children: [
          {
            path: "email",
            component: () => import('../pages/YuQue.vue'),
            meta: {subMenu: "我的邮箱", subMenuIcon: "mdi-email-check-outline", fullPath: "/apps/email"}
          },
          {
            path: "chat",
            component: () => import('../pages/Chat.vue'),
            meta: {subMenu: "聊会儿天", subMenuIcon: "mdi-message-text", fullPath: "/apps/chat", requiresAuth: false}
          },
          {
            path: "todo",
            component: () => import('../pages/Todo.vue'),
            meta: {subMenu: "待办事项", subMenuIcon: "mdi-calendar-check", fullPath: "/apps/todo", requiresAuth: true}
          },
          {
            path: 'photos',
            component: () => import('../pages/Photos.vue'),
            meta: {subMenu: "我的照片", subMenuIcon: "mdi-camera-outline", fullPath: "/apps/photos", requiresAuth: true}
          },
        ]
      },
      {
        path: '/tools',
        meta: {parentMenu: "工具", parentMenuIcon: "mdi-toolbox-outline", hasSub: true},
        children: [
          {
            path: "base64",
            component: () => import('../pages/Base64.vue'),
            meta: {subMenu: "base64", subMenuIcon: "mdi-wrench-clock", fullPath: "/tools/base64"}
          },
        ]
      },
    ]
  },
  {
    path: '/login',
    component: () => import('../pages/Login.vue')
  },
  {
    path: '/initialization',
    component: () => import('../pages/Initialization.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})


router.beforeEach((to, from, next) => {
  console.log(to.fullPath)
  console.log(to.fullPath)
  if (from.fullPath !== "/login" && to.meta.requiresAuth && !localStorage.getItem("token")) {
    next({path: "/login", query: to.path === '/' ? {} : {from: to.path}})
  } else {
    next()
  }

})
export {router, routes}
