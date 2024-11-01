import {createWebHistory, createRouter} from 'vue-router'


const routes = [
  {
    path: '/',
    redirect: '/dashboards',
    component: () => import('../@layouts/default.vue'),
    children: [
      {
        path: '/dashboards',
        redirect: '/dashboards/posts',
        meta: {parentMenu: "首页", parentMenuIcon: "mdi-home"},
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
          },
          {
            path: 'posts',
            redirect: '/dashboards/posts/list',
            meta: {subMenu: "博客", subMenuIcon: "mdi-post-outline", fullPath: "/dashboards/posts"},
            children: [
              {
                path: 'list',
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
                component: () => import('../pages/PostsEditor.vue'),
              },
              {
                path: 'preview/:id',
                component: () => import('../pages/PostsPreview.vue'),
              },
            ]
          },
        ]
      },
      {
        path: '/apps',
        meta: {parentMenu: "我的应用", parentMenuIcon: "mdi-apps"},
        children: [
          {
            path: "email",
            component: () => import('../pages/Email.vue'),
            meta: {subMenu: "我的邮箱", subMenuIcon: "mdi-email-check-outline", fullPath: "/apps/email"}
          },
          {
            path: "chat",
            component: () => import('../pages/Chat.vue'),
            meta: {subMenu: "聊会儿天", subMenuIcon: "mdi-message-text", fullPath: "/apps/chat", requiresAuth: true}
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
        meta: {parentMenu: "工具箱", parentMenuIcon: "mdi-toolbox-outline"},
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
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})


router.beforeEach((to, from, next) => {
  console.log(to.fullPath)
  console.log(to.fullPath)
  if (from.fullPath !== "/login" && to.meta.requiresAuth && !window.localStorage.getItem("token")) {
    next({path: "/login", query: to.path === '/' ? {} : {from: to.path}})
  } else {
    next()
  }
  console.log(to)
  console.log(from)
  console.log(next)

})
export {router, routes}
