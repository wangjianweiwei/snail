import {ref, watch, computed, reactive} from "vue";


const themeConfig = {
  border: ref(true),
  rounded: ref("lg"),
  btnVariant: ref("tonal"),
  elevation: ref(0),
  primaryColor: ref("#268023"),
  dark: ref(true),
  language: ref(["en"])
}

const colors = ["red", "pink", "purple", "deep-purple", "indigo", "blue", "light-blue", "cyan", "teal", "green", "light-green", "lime", "yellow", "amber", "orange", "deep-orange", "brown", "blue-grey", "grey"]

function getRandomColor() {
  const randomIndex = Math.floor(Math.random() * colors.length);
  return colors[randomIndex];
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

export {theme, themeConfig, getRandomColor};

