/**
 * plugins/index.js
 *
 * Automatically included in `./src/main.js`
 */

// Plugins
import vuetify from './vuetify/index'
import {router} from "@/plugins/router";
import i18n from './i18n'
import message from "@/plugins/vuetify/message";


import "@/assets/css/doc.css"
import "@/assets/css/antd.css"
// import "@/assets/css/atom-one-dark.min.css"
import "@/assets/js/react.production.min"
import "@/assets/js/react-dom.production.min"
import "@/assets/js/doc.umd"


export function registerPlugins(app) {
  app.use(i18n)
  app.use(vuetify)
  app.use(message)
  app.use(router)
}
