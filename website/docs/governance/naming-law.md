---
sidebar_position: 2
title: Naming Law
---

# Naming Law

This page prevents drift between symbolic internal naming and public product naming.

## Rule

If both forms are used, define them once and reuse that definition everywhere:

- **Lingos** = symbolic / glyph-native operating layer
- **LingOS** = public framework or product name, if retained

## Do not do this

- switch casing without explanation
- use both names on the same page as if they are interchangeable
- present one name in docs and another in repos with no mapping

## Required references

Every repo, docs page, and public site that mentions this layer should include one of:

- “Lingos (public product name: LingOS)”
- “LingOS (symbolic OS layer: Lingos)”
- or one canonical replacement if the split is removed later

## Future cleanup

If one name is retired, update:
- repo names
- docs nav
- homepage cards
- package names
- screenshots
- external links

---

*Name drift becomes architecture drift if left alone.*
