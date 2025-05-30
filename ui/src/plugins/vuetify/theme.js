export const staticPrimaryColor = '#696CFF'

const theme = {
  defaultTheme: 'dark',
  themes: {
    light: {
      dark: false,
      colors: {
        'primary': '#696CFF',
        'on-primary': '#fff',
        'secondary': '#8592A3',
        'on-secondary': '#fff',
        'success': '#71DD37',
        'on-success': '#fff',
        'info': '#03C3EC',
        'on-info': '#fff',
        'warning': '#FFAB00',
        'on-warning': '#fff',
        'error': '#FF3E1D',
        'background': '#f6f6f6',
        'on-background': '#32475C',
        'surface': '#f6f6f6',
        'on-surface': '#32475C',
        'grey-50': '#f6f6f6',
        'grey-100': '#EBEEF0',
        'grey-200': '#EEEEEE',
        'grey-300': '#E0E0E0',
        'grey-400': '#BDBDBD',
        'grey-500': '#9E9E9E',
        'grey-600': '#757575',
        'grey-700': '#616161',
        'grey-800': '#424242',
        'grey-900': '#212121',
        'perfect-scrollbar-thumb': '#DBDADE',
        'skin-bordered-background': '#fff',
        'skin-bordered-surface': '#fff',
      },
      variables: {
        'code-color': '#d400ff',
        'overlay-scrim-background': '#32475C',
        'overlay-scrim-opacity': 0.5,
        'border-color': '#32475C',
        'snackbar-background': '#32475C',
        'snackbar-color': '#ffffff',
        'tooltip-background': '#262732',
        'tooltip-opacity': 0.9,
        'table-header-background': '#F5F5F7',

        // Shadows
        'shadow-key-umbra-opacity': 'rgba(var(--v-theme-on-surface), 0.06)',
        'shadow-key-penumbra-opacity': 'rgba(var(--v-theme-on-surface), 0.04)',
        'shadow-key-ambient-opacity': 'rgba(var(--v-theme-on-surface), 0.02)',
      },
    },
    dark: {
      dark: true,
      colors: {
        'primary': '#696CFF',
      }
    },
  },
}

export default theme
