// tailwind.config.js
module.exports = {
  content: [
    './templates/**/*.html',
    './templates/**/**/*.html',
    './memories/templates/memories/**/*.html',
    './account/templates/account/**/*.html',
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('daisyui'),
  ],
  daisyui: {
    themes: ['light', 'dark'],
  },
};
