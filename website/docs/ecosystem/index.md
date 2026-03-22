---
sidebar_position: 1
title: Ecosystem Overview
---

# Ecosystem Overview

The MirrorDNA ecosystem is a layered stack for observable, governable AI systems.

## Status block

- **Documentation status**: Public
- **Implementation status**: Mixed by component
- **Use the status matrix**: [Component Status](/status/components)

## Core architecture

```text
Applications
  ├─ Lingos interfaces
  ├─ custom agents
  └─ integrations

Control + observability
  ├─ MirrorDNA Standard
  ├─ ActiveMirrorOS
  ├─ TrustByDesign
  └─ Glyphtrail

Identity + governance
  ├─ AgentDNA
  ├─ Vault Manager
  └─ governance rules
```

## Component roles

### MirrorDNA Standard
The trace and semantics layer.

### ActiveMirrorOS
The runtime, storage, and query layer.

### Lingos / LingOS
The interaction and symbolic execution layer.

### TrustByDesign
The compliance and trust-policy layer.

### AgentDNA
The persona and behavior layer.

### Glyphtrail
The visualization and replay layer.

### Vault Manager
The secure storage and access-control layer.

## Proof rail

Every strong claim on this site should eventually point to one or more of:

- repo
- package
- release
- demo
- benchmark
- SHIPLOG or changelog
- public artifact

Until a proof link is added, treat architectural claims as **design intent**, not guaranteed shipped capability.

## Deployment truth

This page describes the intended ecosystem shape. It does **not** by itself certify current production readiness for every component. Use [Component Status](/status/components) for that.

## Now / Next / Later

### Now
- public docs spine
- ecosystem definitions
- governance cleanup
- status truth

### Next
- per-component proof links
- clearer deployment references
- release-note trail
- source/deploy unification

### Later
- auto-generated proof rails from SHIPLOG
- status badges sourced from repo metadata
- release matrix generated from tags

---

*Architecture pages should explain the stack, not overstate the ship state.*
