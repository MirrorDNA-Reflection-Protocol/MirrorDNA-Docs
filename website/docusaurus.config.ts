// FEU Enforcement: Fact/Estimate/Unknown contract enforced
// Bound to Master Citation v15.2 (Continuity-Perfected Edition)
// © 2025 N1 Intelligence (OPC) Private Limited

import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

const config: Config = {
  title: 'MirrorDNA Ecosystem',
  tagline: 'Trustworthy AI through Observability and Reflection',
  favicon: 'img/favicon.ico',

  // Future flags, see https://docusaurus.io/docs/api/docusaurus-config#future
  future: {
    v4: true, // Improve compatibility with the upcoming Docusaurus v4
  },

  // Set the production url of your site here
  url: 'https://mirrordna-reflection-protocol.github.io',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/MirrorDNA-Docs/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'MirrorDNA-Reflection-Protocol', // Usually your GitHub org/user name.
  projectName: 'MirrorDNA-Docs', // Usually your repo name.

  onBrokenLinks: 'throw',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
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
          // Remove this to remove the "edit this page" links.
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
    // Replace with your project's social card
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
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar',
          position: 'left',
          label: 'Documentation',
        },
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
          title: 'Ecosystem',
          items: [
            {
              label: 'MirrorDNA Standard',
              to: '/mirrordna',
            },
            {
              label: 'ActiveMirrorOS',
              to: '/activemirror',
            },
            {
              label: 'LingOS',
              to: '/lingos',
            },
            {
              label: 'Glyphtrail',
              to: '/glyphtrail',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'GitHub',
              href: 'https://github.com/MirrorDNA-Reflection-Protocol',
            },
            {
              label: 'Discord',
              href: 'https://discord.gg/mirrordna',
            },
          ],
        },
        {
          title: 'More',
          items: [
            {
              label: 'TrustByDesign',
              to: '/trustbydesign',
            },
            {
              label: 'AgentDNA',
              to: '/agentdna',
            },
            {
              label: 'Vault Manager',
              to: '/vault-manager',
            },
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
    algolia: {
      // Placeholder - can be configured later with Algolia DocSearch
      appId: 'YOUR_APP_ID',
      apiKey: 'YOUR_API_KEY',
      indexName: 'mirrordna',
      contextualSearch: true,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
