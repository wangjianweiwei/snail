/**
 * plugins/vuetify.js
 *
 * Framework documentation: https://vuetifyjs.com`
 */

// Styles
import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'
import defaults from '@/plugins/vuetify/defaults'
import {theme} from '@/plugins/vuetify/theme'

// Composables
import {createVuetify} from 'vuetify'
import {VTreeview} from 'vuetify/labs/VTreeview'

// https://vuetifyjs.com/en/introduction/why-vuetify/#feature-guides
export default createVuetify({
  defaults,
  theme,
  components: {
    VTreeview
  },
})
