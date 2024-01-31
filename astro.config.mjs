import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
  site: 'https://diariodibordo.github.io',
  integrations: [starlight({
    title: 'Diario di Bordo',
    locales: {
      root: {
        label: 'Italiano',
        lang: 'it-IT'
      }
    },
    social: {
      github: 'https://github.com/diariodibordo/diariodibordo.github.io'
    },
    sidebar: [{
      label: 'Manuale',
      autogenerate: {
        directory: 'rules'
      },
    }, {
      label: '📝 Logs',
      autogenerate: {
        directory: 'logs'
      }
    }, {
      label: 'Risorse',
      autogenerate: {
        directory: 'resources'
      }
    }]
  })
]
});