# MirrorDNA Ecosystem Documentation

⟡⟦CANONICAL⟧

![Reflective AI Compliance](https://img.shields.io/badge/Reflective_AI-Compliant-brightgreen)
![Master Citation](https://img.shields.io/badge/Master_Citation-v15.2-blue)
![FEU Enforcement](https://img.shields.io/badge/FEU-Enforced-orange)

The unified documentation site for the **MirrorDNA Ecosystem**—a comprehensive suite of tools and frameworks for building trustworthy, observable, and compliant AI systems.

---

## 📜 Bound to Master Citation v15.2

**This documentation set is bound to and governed by:**
**Master Citation v15.2 (Continuity-Perfected Edition)**

All diagrams, architecture descriptions, terminology, and examples must be interpreted through v15.2 governance rules.

### Fact/Estimate/Unknown (FEU) Contract

All outputs from MirrorDNA-based systems adhere to the FEU semantic contract:

- **FACT** — Verifiable, grounded in source material or system state
- **ESTIMATE** — Inferred, probabilistic, or derived through reasoning
- **UNKNOWN** — Explicitly acknowledged gaps in knowledge

This contract ensures **epistemic transparency** and prevents hallucination masquerading as certainty.

---

## ⚠️ Legal Notice

**IMPORTANT:** Please review the [LEGAL_NOTICE.md](./LEGAL_NOTICE.md) before using this documentation or software.

**Key Points:**
- **Research-only** — Not for production use
- **Zero medical advice** — No clinical guidance
- **No autonomy** — Requires human oversight
- **Non-advisory outputs** — Information only, not decision support

© 2025 N1 Intelligence (OPC) Private Limited. All Rights Reserved.

## Overview

This repository contains the complete documentation for all MirrorDNA ecosystem components:

- 🧬 **MirrorDNA Standard**: The foundational specification for AI agent observability
- 🖥️ **ActiveMirrorOS**: Runtime and storage infrastructure for MirrorDNA traces
- 💬 **LingOS**: Conversational AI framework with built-in observability (Lite & Pro)
- ✅ **TrustByDesign**: Compliance and certification framework
- 🎭 **AgentDNA**: Persona engine for consistent agent personalities
- 📊 **Glyphtrail**: Interactive timeline viewer for trace visualization
- 🔐 **Vault Manager**: Enterprise-grade secure storage (LingOS Pro)

## Documentation Stack

This site is built with **Docusaurus**, a modern static site generator optimized for documentation.

**Why Docusaurus?**
- Modern, fast, and responsive
- Built-in search functionality
- Version control integration
- Easy to customize and extend
- Great developer experience

## Prerequisites

- **Node.js** 18.0 or higher
- **npm** 9.0 or higher

## Getting Started

### 1. Install Dependencies

```bash
cd website
npm install
```

### 2. Run Locally

Start the development server:

```bash
npm start
```

The site will open automatically at [http://localhost:3000](http://localhost:3000)

**Features in development mode:**
- Live reload on file changes
- Fast refresh
- Broken link detection

### 3. Build for Production

Create an optimized static build:

```bash
npm run build
```

The static files will be generated in `website/build/`

### 4. Test Production Build Locally

Serve the production build locally:

```bash
npm run serve
```

View at [http://localhost:3000](http://localhost:3000)

## Project Structure

```
MirrorDNA-Docs/
├── README.md                    # This file
├── website/                     # Docusaurus site root
│   ├── docs/                    # Documentation content
│   │   ├── intro.md            # Homepage
│   │   ├── mirrordna/          # MirrorDNA Standard docs
│   │   │   ├── index.md
│   │   │   ├── semantics.md
│   │   │   └── use-cases.md
│   │   ├── activemirror/       # ActiveMirrorOS docs
│   │   │   ├── index.md
│   │   │   └── getting-started.md
│   │   ├── lingos/             # LingOS docs
│   │   │   └── index.md
│   │   ├── trustbydesign/      # TrustByDesign docs
│   │   │   └── index.md
│   │   ├── agentdna/           # AgentDNA docs
│   │   │   └── index.md
│   │   ├── glyphtrail/         # Glyphtrail docs
│   │   │   └── index.md
│   │   ├── vault-manager/      # Vault Manager docs
│   │   │   └── index.md
│   │   └── ecosystem/          # Ecosystem overview
│   │       └── index.md
│   ├── src/                    # React components
│   ├── static/                 # Static assets
│   ├── docusaurus.config.ts    # Site configuration
│   ├── sidebars.ts            # Sidebar configuration
│   └── package.json           # Dependencies
└── .git/                       # Git repository
```

## Documentation Sections

### MirrorDNA Standard
Core specification for AI agent observability and reflection. Defines trace format, event types, and semantic annotations.

**Key pages:**
- Overview and concepts
- Semantic annotations
- Use cases and examples

### ActiveMirrorOS
Infrastructure layer for collecting, storing, and querying MirrorDNA traces.

**Key pages:**
- System overview
- Getting started guide
- Deployment options

### LingOS
Conversational AI framework with native MirrorDNA support.

**Key pages:**
- Lite vs Pro comparison
- Quick start guide
- Integration examples

### TrustByDesign
Compliance framework supporting GDPR, HIPAA, SOC2, and more.

**Key pages:**
- Supported frameworks
- Automated compliance checking
- Audit reporting

### AgentDNA
Persona engine for defining and versioning agent personalities.

**Key pages:**
- Creating personas
- Testing and validation
- Persona marketplace

### Glyphtrail
Interactive visualization tool for exploring MirrorDNA traces.

**Key pages:**
- Timeline, graph, and table views
- Trace comparison
- Replay mode

### Vault Manager
Enterprise security features for LingOS Pro users.

**Key pages:**
- Encryption and access control
- Compliance profiles
- Deployment options

### Ecosystem Overview
High-level view of how all components work together.

**Key pages:**
- Architecture overview
- Integration patterns
- Deployment architectures

## Deploying to GitHub Pages

### Automatic Deployment (Recommended)

GitHub Actions will automatically deploy to GitHub Pages when you push to the main branch.

1. Enable GitHub Pages in repository settings:
   - Go to Settings > Pages
   - Source: Deploy from a branch
   - Branch: `gh-pages` / `root`

2. Push to main branch:
   ```bash
   git add .
   git commit -m "Update documentation"
   git push origin main
   ```

3. GitHub Actions will automatically build and deploy

### Manual Deployment

Deploy manually using the Docusaurus deployment command:

```bash
cd website

# Set GitHub credentials (if not already configured)
export GIT_USER=<Your GitHub username>

# Deploy
npm run deploy
```

This will:
1. Build the static site
2. Push to the `gh-pages` branch
3. Trigger GitHub Pages deployment

### Deployment Configuration

The deployment is configured in `docusaurus.config.ts`:

```typescript
{
  url: 'https://mirrordna-reflection-protocol.github.io',
  baseUrl: '/MirrorDNA-Docs/',
  organizationName: 'MirrorDNA-Reflection-Protocol',
  projectName: 'MirrorDNA-Docs',
}
```

## Contributing

### Adding New Documentation

1. Create a new markdown file in the appropriate section:
   ```bash
   touch website/docs/mirrordna/new-page.md
   ```

2. Add frontmatter:
   ```markdown
   ---
   sidebar_position: 3
   title: New Page Title
   ---

   # Content here
   ```

3. The page will automatically appear in the sidebar

### Editing Existing Documentation

1. Find the markdown file in `website/docs/`
2. Edit the content
3. Save and the dev server will hot-reload

### Adding Images

1. Place images in `website/static/img/`
2. Reference in markdown:
   ```markdown
   ![Alt text](/img/your-image.png)
   ```

### Custom Components

Create React components in `website/src/components/` and import them in markdown:

```jsx
import MyComponent from '@site/src/components/MyComponent';

<MyComponent />
```

## Search Configuration

The site is configured for Algolia DocSearch (placeholder configuration included).

To enable search:

1. Apply for [Algolia DocSearch](https://docsearch.algolia.com/apply/)
2. Once approved, update `docusaurus.config.ts`:
   ```typescript
   algolia: {
     appId: 'YOUR_ACTUAL_APP_ID',
     apiKey: 'YOUR_ACTUAL_API_KEY',
     indexName: 'mirrordna',
   }
   ```

Alternatively, use the built-in local search plugin.

## Customization

### Theming

Edit `website/src/css/custom.css` to customize:
- Colors
- Fonts
- Spacing
- Component styles

### Navigation

Edit `website/docusaurus.config.ts` to customize:
- Navbar items
- Footer links
- External links

### Sidebar

Edit `website/sidebars.ts` for manual sidebar configuration (currently using auto-generated sidebars).

## Maintenance

### Updating Dependencies

```bash
cd website
npm update
```

### Checking for Broken Links

```bash
npm run build
# Docusaurus will report broken links during build
```

### Clearing Cache

```bash
npm run clear
npm run start
```

## Troubleshooting

### Port 3000 Already in Use

```bash
npm start -- --port 3001
```

### Build Errors

Clear cache and rebuild:
```bash
npm run clear
rm -rf node_modules
npm install
npm run build
```

### Deployment Failures

Check GitHub Actions logs in the repository's Actions tab.

## Support & Community

- **GitHub Issues**: [Report bugs or request features](https://github.com/MirrorDNA-Reflection-Protocol/MirrorDNA-Docs/issues)
- **Discussions**: [Ask questions](https://github.com/MirrorDNA-Reflection-Protocol/discussions)
- **Discord**: [Join the community](https://discord.gg/mirrordna)

## License

Documentation content is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

Code examples are licensed under [MIT](https://opensource.org/licenses/MIT)

---

**Built with ❤️ by the MirrorDNA community**
