---
sidebar_position: 1
title: Ecosystem Overview
---

# Ecosystem Overview

The **MirrorDNA Ecosystem** is a comprehensive suite of tools and frameworks that work together to enable trustworthy, observable, and compliant AI systems.

## The Big Picture

```
┌─────────────────────────────────────────────────────────────┐
│                    APPLICATION LAYER                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   LingOS     │  │  Custom      │  │  LangChain   │      │
│  │   Agents     │  │  Agents      │  │  + Plugin    │      │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘      │
│         │                 │                 │               │
│         └─────────────────┴─────────────────┘               │
│                           │                                 │
│                           ↓                                 │
│         ┌──────────────────────────────────┐                │
│         │      MirrorDNA Standard          │                │
│         │   (Trace Specification)          │                │
│         └─────────────┬────────────────────┘                │
│                       │                                     │
│    ┌──────────────────┼──────────────────┐                 │
│    │                  │                  │                 │
│    ↓                  ↓                  ↓                 │
│  ┌──────────┐   ┌──────────┐      ┌──────────┐            │
│  │ AgentDNA │   │TrustBy   │      │Glyphtrail│            │
│  │(Personas)│   │ Design   │      │(Visualiz)│            │
│  └──────────┘   └──────────┘      └──────────┘            │
│                                                             │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ↓
┌─────────────────────────────────────────────────────────────┐
│                   INFRASTRUCTURE LAYER                       │
│                                                              │
│         ┌──────────────────────────────────┐                │
│         │     ActiveMirrorOS               │                │
│         │   (Runtime & Storage)            │                │
│         └──────────────┬───────────────────┘                │
│                        │                                    │
│         ┌──────────────┴───────────────┐                    │
│         │                              │                    │
│         ↓                              ↓                    │
│  ┌──────────────┐              ┌──────────────┐            │
│  │  Open Source │              │Vault Manager │            │
│  │   Storage    │              │  (Pro/Ent)   │            │
│  └──────────────┘              └──────────────┘            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Core Components

### 1. MirrorDNA Standard

**Role**: Foundation—the "language" of AI observability

**What it does**:
- Defines trace format and semantics
- Ensures interoperability across tools
- Provides specification for implementations

**Learn more**: [MirrorDNA Standard](/mirrordna)

### 2. ActiveMirrorOS

**Role**: Infrastructure—the "runtime" for traces

**What it does**:
- Collects traces from agents in real-time
- Stores and indexes traces efficiently
- Provides query APIs
- Manages retention and archival

**Learn more**: [ActiveMirrorOS](/activemirror)

### 3. LingOS

**Role**: Framework—"batteries-included" agent builder

**What it does**:
- Build conversational AI agents
- Automatic MirrorDNA tracing
- Lite (open-source) and Pro (enterprise) editions
- RAG, tools, multi-agent support

**Learn more**: [LingOS](/lingos)

### 4. TrustByDesign

**Role**: Compliance—automated regulatory adherence

**What it does**:
- Analyzes traces for compliance
- Generates audit reports
- Monitors for violations
- Supports GDPR, HIPAA, SOC2, etc.

**Learn more**: [TrustByDesign](/trustbydesign)

### 5. AgentDNA

**Role**: Personas—consistent agent personalities

**What it does**:
- Define agent personalities and behaviors
- Version and test personas
- Marketplace for pre-built personas
- MirrorDNA-traced persona activation

**Learn more**: [AgentDNA](/agentdna)

### 6. Glyphtrail

**Role**: Visualization—make traces understandable

**What it does**:
- Interactive trace explorer
- Timeline, graph, and table views
- Trace comparison and replay
- Export and sharing

**Learn more**: [Glyphtrail](/glyphtrail)

### 7. Vault Manager / LingOS Pro

**Role**: Security—enterprise-grade protection

**What it does**:
- Encrypted trace storage
- Access control and RBAC
- Compliance profiles
- Backup and disaster recovery

**Learn more**: [Vault Manager](/vault-manager)

## How Components Work Together

### End-to-End Flow

```
1. Developer creates agent with LingOS
      ↓
2. Agent uses AgentDNA persona
      ↓
3. Agent executes, generates MirrorDNA traces
      ↓
4. ActiveMirrorOS collects and stores traces
      ↓
5. TrustByDesign checks compliance in real-time
      ↓
6. Glyphtrail visualizes for debugging
      ↓
7. Vault Manager (Pro) encrypts and secures
```

### Example: Customer Support Agent

```python
# Step 1: Load persona
from agentdna import load_persona
persona = load_persona("customer_support.yaml")

# Step 2: Create LingOS agent with persona
from lingos import Agent
agent = Agent(
    model="gpt-4",
    persona=persona,
    activemirror_url="http://localhost:8080"
)

# Step 3: Agent processes customer query
response = agent.chat("I want a refund")
# → Generates MirrorDNA trace
# → Sent to ActiveMirrorOS
# → Checked by TrustByDesign
# → Viewable in Glyphtrail

# Step 4: Compliance team reviews
from trustbydesign import ComplianceChecker
checker = ComplianceChecker(framework="GDPR")
result = checker.check_trace(agent.last_trace_id)
# → Ensures GDPR compliance

# Step 5: Developer debugs if needed
# Open Glyphtrail at http://localhost:3000
# → Visual timeline of agent decision-making
```

## Integration Patterns

### Pattern 1: Full Stack

Use all components for maximum capability:

```
LingOS + AgentDNA + ActiveMirrorOS + 
TrustByDesign + Glyphtrail + Vault Manager (Pro)
```

**Best for**: Enterprise production deployments

### Pattern 2: Open Source Core

Use free components:

```
Custom Agent + MirrorDNA SDK + ActiveMirrorOS + Glyphtrail
```

**Best for**: Startups, research, learning

### Pattern 3: Compliance-First

Focus on regulatory requirements:

```
LingOS + ActiveMirrorOS + TrustByDesign + Vault Manager
```

**Best for**: Healthcare, finance, government

### Pattern 4: Developer Tools

Emphasis on development experience:

```
LingOS Lite + ActiveMirrorOS + Glyphtrail
```

**Best for**: Development and testing

## Deployment Architectures

### Local Development

```
┌──────────────────┐
│  Developer Laptop│
│                  │
│  • LingOS Agent  │
│  • ActiveMirror  │
│    (Docker)      │
│  • Glyphtrail    │
│    (Docker)      │
└──────────────────┘
```

```bash
# docker-compose.yml
services:
  activemirror:
    image: mirrordna/activemirror
  glyphtrail:
    image: mirrordna/glyphtrail
  # Your agent runs locally
```

### Cloud Production (AWS)

```
┌─────────────────────────────────────┐
│              AWS Cloud              │
│                                     │
│  ┌──────────────────────────────┐   │
│  │ ECS/EKS: LingOS Agents       │   │
│  └────────────┬─────────────────┘   │
│               │                     │
│               ↓                     │
│  ┌──────────────────────────────┐   │
│  │ ActiveMirrorOS (EKS)         │   │
│  │ • RDS PostgreSQL             │   │
│  │ • S3 cold storage            │   │
│  └────────────┬─────────────────┘   │
│               │                     │
│               ↓                     │
│  ┌──────────────────────────────┐   │
│  │ TrustByDesign (Lambda)       │   │
│  └────────────┬─────────────────┘   │
│               │                     │
│               ↓                     │
│  ┌──────────────────────────────┐   │
│  │ Vault Manager (Pro)          │   │
│  │ • KMS encryption             │   │
│  │ • S3 encrypted backups       │   │
│  └──────────────────────────────┘   │
│                                     │
│  ┌──────────────────────────────┐   │
│  │ Glyphtrail (CloudFront+S3)   │   │
│  └──────────────────────────────┘   │
└─────────────────────────────────────┘
```

### Hybrid (Data On-Prem)

```
┌──────────────────┐         ┌──────────────────┐
│   Cloud          │         │  On-Premises     │
│                  │         │                  │
│ • LingOS Agents  │────────▶│ • ActiveMirror   │
│ • Glyphtrail UI  │◀────────│ • Vault Manager  │
│                  │  VPN    │ • Databases      │
└──────────────────┘         └──────────────────┘
```

## Technology Stack

### Languages & Runtimes

- **Python**: Primary SDK, ActiveMirrorOS core
- **TypeScript/JavaScript**: SDKs, Glyphtrail frontend
- **Go**: High-performance components
- **Rust**: Critical path optimizations

### Storage

- **TimescaleDB**: Time-series trace storage
- **PostgreSQL**: Metadata and relations
- **ClickHouse**: Analytics queries
- **S3/Blob**: Cold storage, backups

### Frontend

- **React**: Glyphtrail UI
- **D3.js**: Visualizations
- **TailwindCSS**: Styling
- **Docusaurus**: Documentation (this site!)

### Infrastructure

- **Docker**: Containerization
- **Kubernetes**: Orchestration
- **Terraform**: Infrastructure as code
- **GitHub Actions**: CI/CD

## Versioning & Compatibility

### MirrorDNA Spec Versions

- **v1.0**: Initial specification
- **v1.1**: Added semantic annotations
- **v2.0**: (Upcoming) Multi-modal support

### Component Compatibility Matrix

| Component | MirrorDNA Spec | Min ActiveMirror | Min Python | Min Node.js |
|-----------|----------------|------------------|------------|-------------|
| **ActiveMirrorOS 1.x** | v1.0-v1.1 | - | 3.8+ | 16+ |
| **LingOS Lite 1.x** | v1.0-v1.1 | 1.0+ | 3.9+ | - |
| **LingOS Pro 1.x** | v1.0-v1.1 | 1.0+ | 3.9+ | - |
| **Glyphtrail 1.x** | v1.0-v1.1 | 1.0+ | - | 18+ |
| **TrustByDesign 1.x** | v1.0-v1.1 | 1.0+ | 3.9+ | - |
| **AgentDNA 1.x** | v1.0-v1.1 | 1.0+ | 3.9+ | 18+ |

## Roadmap

### Q2 2024

- **MirrorDNA v2.0**: Multi-modal traces (images, audio)
- **ActiveMirrorOS**: Distributed tracing across agents
- **LingOS**: Voice agent support
- **Glyphtrail**: 3D visualization for complex systems

### Q3 2024

- **TrustByDesign**: AI Act certification automation
- **AgentDNA**: Persona learning from feedback
- **Vault Manager**: FedRAMP compliance

### Q4 2024

- **Ecosystem**: Cross-agent coordination
- **MirrorDNA**: Real-time streaming protocol
- **ActiveMirrorOS**: Global distribution

## Community & Contributions

### Open Source

Most components are open source (MIT license):
- MirrorDNA Standard
- ActiveMirrorOS
- LingOS Lite
- Glyphtrail
- AgentDNA

**Contribute**:
- GitHub: [MirrorDNA-Reflection-Protocol](https://github.com/MirrorDNA-Reflection-Protocol)
- Discussions: Share ideas and feedback
- Issues: Report bugs and request features

### Commercial

Enterprise features available in:
- LingOS Pro
- Vault Manager
- Enterprise support

**Contact**: [enterprise@mirrordna.org](mailto:enterprise@mirrordna.org)

## Getting Started

### 1. Learn the Basics

Start with the [MirrorDNA Standard](/mirrordna) to understand core concepts.

### 2. Try Locally

```bash
# Clone quickstart repo
git clone https://github.com/MirrorDNA-Reflection-Protocol/quickstart
cd quickstart

# Start all services
docker-compose up -d

# Run example agent
python examples/simple_agent.py

# View traces at http://localhost:3000
```

### 3. Build Your First Agent

Follow the [LingOS tutorial](/lingos) to create a simple agent.

### 4. Add Compliance

Integrate [TrustByDesign](/trustbydesign) for compliance checking.

### 5. Deploy to Production

Follow deployment guides for your platform (see component-specific documentation).

## Support & Resources

### Documentation

- **This Site**: Comprehensive guides and API docs
- **GitHub Wikis**: Detailed technical documentation
- **API References**: Auto-generated from code

### Community

- **Discord**: [Join chat](https://discord.gg/mirrordna)
- **GitHub Discussions**: [Ask questions](https://github.com/MirrorDNA-Reflection-Protocol/discussions)
- **Stack Overflow**: Tag `mirrordna`

### Enterprise

- **Email**: [support@mirrordna.org](mailto:support@mirrordna.org)
- **Slack Connect**: For Pro customers
- **24/7 Support**: Enterprise tier

## Comparison with Alternatives

| Feature | MirrorDNA Ecosystem | LangSmith | Weights & Biases | Helicone |
|---------|---------------------|-----------|------------------|----------|
| **Open Source** | ✅ Core components | ❌ | ⚠️ Partial | ❌ |
| **Self-Hosted** | ✅ | ⚠️ Enterprise only | ⚠️ | ❌ |
| **Compliance** | ✅ Built-in | ⚠️ Basic | ⚠️ Basic | ❌ |
| **Visualization** | ✅ Glyphtrail | ✅ | ✅ | ⚠️ Basic |
| **Multi-Framework** | ✅ | ⚠️ LangChain focus | ✅ | ✅ |
| **Persona Engine** | ✅ AgentDNA | ❌ | ❌ | ❌ |
| **Encryption** | ✅ Vault Manager | ⚠️ Enterprise | ❌ | ❌ |

## Success Stories

### Case Study: Healthcare AI

**Challenge**: Deploy HIPAA-compliant AI for patient communication

**Solution**: LingOS Pro + TrustByDesign + Vault Manager

**Results**:
- ✅ HIPAA certification in 6 weeks
- ✅ 40% reduction in support costs
- ✅ Zero compliance violations in 1 year

### Case Study: Financial Services

**Challenge**: Explainable AI for loan decisions (regulatory requirement)

**Solution**: MirrorDNA + ActiveMirrorOS + Glyphtrail

**Results**:
- ✅ Passed regulatory audit
- ✅ 90% faster investigation of disputes
- ✅ Improved model by analyzing traces

### Case Study: E-commerce

**Challenge**: Scale customer support AI to 10M conversations/month

**Solution**: LingOS + ActiveMirrorOS + AgentDNA

**Results**:
- ✅ Handled scale effortlessly
- ✅ Consistent brand voice across agents
- ✅ 25% improvement in CSAT scores

---

*Building the future of trustworthy AI, together.* 🌐
