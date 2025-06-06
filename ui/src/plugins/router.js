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
        meta: {parentMenu: "menu.title.blog", parentMenuIcon: "mdi-post-outline", fullPath: "/posts", hasSub: false},
        children: [
          {
            path: 'list',
            meta: {requiresAuth: false},
            component: () => import('../pages/PostsList.vue'),
          },
          {
            path: 'timeline',
            component: () => import('../pages/PostTimeline.vue'),
          },
          {
            path: 'editor/:id',
            meta: {requiresAuth: true},
            component: () => import('../pages/PostsEditor.vue'),
          },
          {
            path: 'reader/:id',
            meta: {requiresAuth: false},
            component: () => import('../pages/PostsReader.vue'),
          },
        ]
      },
      {
        path: '/about',
        redirect: '/about/me',
        meta: {parentMenu: "menu.title.about", parentMenuIcon: "mdi-information-variant", fullPath:"/about", hasSub: false},
        children: [
          {
            path: "me",
            component: () => import('../pages/About.vue'),
          }
        ]
      },
      {
        path: '/apps',
        meta: {parentMenu: "menu.title.apps", parentMenuIcon: "mdi-apps", hasSub: true},
        children: [
          {
            path: "email",
            component: () => import('../pages/Email.vue'),
            meta: {subMenu: "menu.subtitle.email", subMenuIcon: "mdi-email-check-outline", fullPath: "/apps/email"}
          },
          {
            path: "chat",
            component: () => import('../pages/Chat.vue'),
            meta: {subMenu: "menu.subtitle.chat", subMenuIcon: "mdi-message-text", fullPath: "/apps/chat", requiresAuth: false}
          },
          {
            path: "todo",
            component: () => import('../pages/Todo.vue'),
            meta: {subMenu: "menu.subtitle.todo", subMenuIcon: "mdi-calendar-check", fullPath: "/apps/todo", requiresAuth: true}
          },
          {
            path: 'photos',
            component: () => import('../pages/Photos.vue'),
            meta: {subMenu: "menu.subtitle.photos", subMenuIcon: "mdi-camera-outline", fullPath: "/apps/photos", requiresAuth: true}
          },
          {
            path: "password",
            component: () => import('../pages/PasswordManage.vue'),
            meta: {subMenu: "menu.subtitle.password", subMenuIcon: 'mdi-key-chain', fullPath: '/apps/password', requiresAuth: true}
          }
        ]
      },
      {
        path: '/tools',
        meta: {parentMenu: "menu.title.tools", parentMenuIcon: "mdi-tools", hasSub: true},
        children: [
          {
            path: "base64",
            component: () => import('../pages/Base64.vue'),
            meta: {subMenu: "menu.subtitle.base64", subMenuIcon: "mdi-wrench-clock", fullPath: "/tools/base64"}
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
  if (from.fullPath !== "/login" && to.meta.requiresAuth && !localStorage.getItem("token")) {
    next({path: "/login", query: to.path === '/' ? {} : {from: to.path}})
  } else {
    next()
  }

})
export {router, routes}
