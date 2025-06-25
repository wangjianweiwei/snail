// i18n.ts
import {createI18n} from 'vue-i18n'
import zh from './locales/zh.json'
import en from './locales/en.json'
import {themeConfig} from "@/plugins/vuetify/theme";


console.log(themeConfig.language.value, "????")
const i18n = createI18n({
  legacy: false, // 使用 Composition API 模式
  locale: themeConfig.language.value[0],
  fallbackLocale: 'zh',
  messages: {en, zh},
})

export default i18n
