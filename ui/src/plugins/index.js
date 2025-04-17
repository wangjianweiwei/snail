/**
 * plugins/index.js
 *
 * Automatically included in `./src/main.js`
 */

// Plugins
import vuetify from './vuetify/index'
import {router} from "@/plugins/router";
import "quill/dist/quill.snow.css";


import "quill/dist/quill.core.css"
import "@/quill-snow.less"
import "@/assets/css/doc.css"
import "@/assets/css/antd.css"
import "@/assets/css/atom-one-dark.min.css"
import "@/assets/js/react.production.min"
import "@/assets/js/react-dom.production.min"
import "@/assets/js/doc.umd"


export function registerPlugins(app) {
  app.use(vuetify)
  app.use(router)
}
