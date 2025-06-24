import {ref, watch, computed, reactive} from "vue";


const themeConfig = {
  border: ref(false),
  rounded: ref("lg"),
  btnVariant: ref("tonal"),
  elevation: ref(0),
  primaryColor: ref("#696CFF"),
  dark: ref(true),
  language: ref(["zh"])
}

const saved = JSON.parse(localStorage.getItem('themeConfig') || '{}')
for (const key in saved) {
  if (themeConfig[key]) {
    themeConfig[key].value = saved[key]
  }
}


for (const key in themeConfig) {
  watch(themeConfig[key], (newVal) => {
    const current = JSON.parse(localStorage.getItem('themeConfig') || '{}')
    current[key] = newVal
    console.log(key, newVal)
    localStorage.setItem('themeConfig', JSON.stringify(current))
  })
}


const theme = {
  defaultTheme: themeConfig.dark.value ? 'dark' : 'light',
  themes: {
    light: {
      dark: false, colors: {
        primary: themeConfig.primaryColor,
      },
    }, dark: {
      dark: true, colors: {
        primary: themeConfig.primaryColor
      }
    },
  },
}

export {theme, themeConfig};

