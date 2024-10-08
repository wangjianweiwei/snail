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
        meta: {parentMenu: "Dashboards", parentMenuIcon: "mdi-home"},
        children: [
          {
            path: "profile",
            component: () => import('../pages/UserProfile.vue'),
            meta: {subMenu: "profile", subMenuIcon: "mdi-account-outline", fullPath: "/dashboards/profile", requiresAuth: true}
          },
          {
            path: "settings",
            component: () => import('../pages/Settings.vue'),
            meta: {subMenu: "settings", subMenuIcon: "mdi-cogs", fullPath: "/dashboards/settings"}
          },
          {
            path: 'posts',
            component: () => import('../pages/Posts.vue'),
            meta: {subMenu: "posts", subMenuIcon: "mdi-post-outline", fullPath: "/dashboards/posts"},
          },
          {
            path: 'posts/:id/compose',
            component: () => import('../pages/PostsEditor.vue'),
          },
          {
            path: 'posts/:id/preview',
            component: () => import('../pages/PostsPreview.vue'),
          },
        ]
      },
      {
        path: '/apps',
        meta: {parentMenu: "Apps", parentMenuIcon: "mdi-apps"},
        children: [
          {
            path: "email",
            component: () => import('../pages/Email.vue'),
            meta: {subMenu: "email", subMenuIcon: "mdi-email-check-outline", fullPath: "/apps/email"}
          },
          {
            path: "chat",
            component: () => import('../pages/Chat.vue'),
            meta: {subMenu: "chat", subMenuIcon: "mdi-message-text", fullPath: "/apps/chat", requiresAuth: true}
          },
          {
            path: "todo",
            component: () => import('../pages/Todo.vue'),
            meta: {subMenu: "todo", subMenuIcon: "mdi-calendar-check", fullPath: "/apps/todo", requiresAuth: true}
          },
          {
            path: 'photos',
            component: () => import('../pages/Photos.vue'),
            meta: {subMenu: "photos", subMenuIcon: "mdi-camera-outline", fullPath: "/apps/photos", requiresAuth: true}
          },
        ]
      },
      {
        path: '/tools',
        meta: {parentMenu: "Tools", parentMenuIcon: "mdi-toolbox-outline"},
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


router.beforeEach((to, from,next) => {
  console.log(to.fullPath)
  console.log(to.fullPath)
  if (from.fullPath !== "/login" && to.meta.requiresAuth && !window.localStorage.getItem("token")) {
    next({path: "/login", query: to.path === '/' ? {} : { from: to.path }})
  }else {
      next()
  }
  console.log(to)
  console.log(from)
  console.log(next)

})
export {router, routes}
