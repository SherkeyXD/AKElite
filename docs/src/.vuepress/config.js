const { description } = require('../../package')

module.exports = {
  title: 'AKElite 方舟敌人精英查询',
  description: '这是一个用于快速查询方舟中哪些敌人为精英的网站',
  head: [
    ['link', { rel: 'icon', href: '/logo/1024x.png' }],
    ['link', { rel: 'manifest', href: '/manifest.json' }],
    ['meta', { name: 'theme-color', content: '#3eaf7c' }],
    ['meta', { name: 'apple-mobile-web-app-capable', content: 'yes' }],
    ['meta', { name: 'apple-mobile-web-app-status-bar-style', content: 'black' }],
    ['link', { rel: 'apple-touch-icon', href: '/icons/apple-touch-icon-152x152.png' }],
    ['link', { rel: 'mask-icon', href: '/icons/safari-pinned-tab.svg', color: '#3eaf7c' }],
    ['meta', { name: 'msapplication-TileImage', content: '/icons/msapplication-icon-144x144.png' }],
    ['meta', { name: 'msapplication-TileColor', content: '#000000' }]
  ],
  /**
   * Theme configuration, here is the default theme configuration for VuePress.
   *
   * ref：https://v1.vuepress.vuejs.org/theme/default-theme-config.html
   */
  themeConfig: {
    repo: '',
    editLinks: false,
    docsDir: '',
    editLinkText: '',
    lastUpdated: false,
    nav: [
      {
        text: '项目介绍',
        link: '/intro',
      },
      {
        text: '敌人信息',
        link: '/enemy/',
      },
      {
        text: 'Github repo',
        link: 'https://github.com/SherkeyXD/AKElite',
      },
      {
        text: 'PRTS Wiki',
        link: 'https://prts.wiki'
      }
    ],
    sidebar: {
      'intro': '/intro.md',
      '/enemy/': [
        {
          title: '敌人信息',
          collapsable: false,
          children: [
            'normal',
            'elite',
            'boss',
          ]
        }
      ],
    }
  },

  /**
   * Apply plugins，ref：https://v1.vuepress.vuejs.org/zh/plugin/
   */
  plugins: [
    '@vuepress/plugin-back-to-top',
    '@vuepress/plugin-medium-zoom',
    ['@vuepress/search', {
      searchMaxSuggestions: 10
    }],
    ['@vuepress/pwa', {
      serviceWorker: true,
      updatePopup: true
    }],
  ]
}
