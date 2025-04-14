/**
 * main.js
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Plugins
import { registerPlugins } from '@/plugins'

// Components
import App from './App.vue'

// Composables
import { createApp } from 'vue'
import "@/assets/css/antd.css"
import "@/assets/css/doc.css"
import "@/assets/js/react.production.min"
import "@/assets/js/react-dom.production.min"
import "@/assets/js/doc.umd"

const app = createApp(App)

registerPlugins(app)

app.mount('#app')
