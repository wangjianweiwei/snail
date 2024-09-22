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


export function registerPlugins(app) {
  app.use(vuetify)
  app.use(router)
}
