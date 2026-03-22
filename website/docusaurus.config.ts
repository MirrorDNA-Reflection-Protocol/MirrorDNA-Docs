import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'MirrorDNA',
  tagline: 'Trustworthy AI through observability, continuity, and governed execution',
  favicon: 'img/favicon.ico',

  future: {
    v4: true,
  },

  url: 'https://mirrordna-reflection-protocol.github.io',
  baseUrl: '/MirrorDNA-Docs/',

  organizationName: 'MirrorDNA-Reflection-Protocol',
  projectName: 'MirrorDNA-Docs',

  onBrokenLinks: 'throw',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          routeBasePath: '/',
          editUrl:
            'https://github.com/MirrorDNA-Reflection-Protocol/MirrorDNA-Docs/tree/main/website/',
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    image: 'img/docusaurus-social-card.jpg',
    colorMode: {
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: 'MirrorDNA',
      logo: {
        alt: 'MirrorDNA Logo',
        src: 'img/logo.svg',
      },
      items: [
        {to: '/', label: 'Home', position: 'left'},
        {to: '/ecosystem', label: 'Ecosystem', position: 'left'},
        {to: '/status', label: 'Status', position: 'left'},
        {to: '/governance/source-of-truth', label: 'Governance', position: 'left'},
        {
          href: 'https://github.com/MirrorDNA-Reflection-Protocol',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Core',
          items: [
            {label: 'MirrorDNA Standard', to: '/mirrordna'},
            {label: 'ActiveMirrorOS', to: '/activemirror'},
            {label: 'Lingos / LingOS', to: '/lingos'},
          ],
        },
        {
          title: 'Governance',
          items: [
            {label: 'Source of Truth', to: '/governance/source-of-truth'},
            {label: 'Naming Law', to: '/governance/naming-law'},
            {label: 'Component Status', to: '/status/components'},
          ],
        },
        {
          title: 'More',
          items: [
            {label: 'TrustByDesign', to: '/trustbydesign'},
            {label: 'AgentDNA', to: '/agentdna'},
            {label: 'Vault Manager', to: '/vault-manager'},
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} MirrorDNA Reflection Protocol. Built with Docusaurus.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
      additionalLanguages: ['python', 'javascript', 'typescript', 'bash', 'yaml', 'json'],
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
