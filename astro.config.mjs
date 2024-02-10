import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

import tailwind from "@astrojs/tailwind";

// https://astro.build/config
export default defineConfig({
  site: 'https://diariodibordo.github.io',
  integrations: [starlight({
    title: 'Diario di Bordo',
    // rendero pubblico il progetto open-source una volta sicuro
    editLink: {
      baseUrl: 'https://github.com/diariodibordo/diariodibordo.github.io/tree/main'
    },
    customCss:[
      './src/tailwind.css',
    ],
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
      }
    },{
      label: 'Classi',
      badge: 'WIP',
      autogenerate: {
        directory: '/classi'
      }
    }, {
      label: 'Logs',
      autogenerate: {
        directory: 'logs'
      }
    }, {
      label: 'Risorse',
      autogenerate: {
        directory: 'resources'
      }
    }
  ]
  }), tailwind({
    applyBaseStyles: false,
  })]
});