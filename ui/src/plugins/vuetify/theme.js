import {ref} from "vue";

const primaryColor = ref("#696CFF")

const theme = {
  defaultTheme: 'dark',
  themes: {
    light: {
      dark: false,
      colors: {
        'primary': primaryColor
      },
    },
    dark: {
      dark: true,
      colors: {
        'primary': primaryColor
      }
    },
  },
}

export {theme, primaryColor};

