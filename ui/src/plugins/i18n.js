// i18n.ts
import {createI18n} from 'vue-i18n'
import zh from './locales/zh.json'
import en from './locales/en.json'

const messages = {
  en,
  zh
}

const i18n = createI18n({
  legacy: false, // 使用 Composition API 模式
  locale: 'zh',
  fallbackLocale: 'en',
  messages,
})

export default i18n
