import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

import tailwind from "@astrojs/tailwind";

// https://astro.build/config
export default defineConfig({
  site: 'https://diariodibordo.github.io',
  integrations: [starlight({
    title: 'Diario di Bordo',
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
  }), tailwind({
    applyBaseStyles: false,
  })]
});