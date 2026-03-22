import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  tutorialSidebar: [
    'intro',
    {
      type: 'category',
      label: 'Core',
      items: [
        'ecosystem/index',
        'mirrordna/index',
        'activemirror/index',
        'lingos/index',
      ],
    },
    {
      type: 'category',
      label: 'Trust + Security',
      items: [
        'trustbydesign/index',
        'vault-manager/index',
        'status/index',
        'status/components',
      ],
    },
    {
      type: 'category',
      label: 'Governance',
      items: [
        'governance/source-of-truth',
        'governance/naming-law',
      ],
    },
    {
      type: 'category',
      label: 'Extensions',
      items: [
        'agentdna/index',
        'glyphtrail/index',
      ],
    },
  ],
};

export default sidebars;
