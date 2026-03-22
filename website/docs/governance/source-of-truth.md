---
sidebar_position: 1
title: Source of Truth
---

# Source of Truth

This page defines how public documentation, generated artifacts, and live deployment relate to each other.

## Canonical rule

There must be one explicit answer to each of these:

1. Which branch is canonical for docs source?
2. Which branch or artifact is deployed to GitHub Pages?
3. Is SHIPLOG generating pages, partial pages, or metrics only?
4. What should a contributor edit if they want to change the live site?

## Required deployment note

Document this in the repo root and in the deployment workflow.

## Minimal deployment contract

- `main` contains source docs
- `gh-pages` contains built output only
- generated metrics must state their generator source
- live pages must not silently diverge from repo content

## If SHIPLOG is involved

If the site is partially generated from SHIPLOG, add:

- generator source path
- generator inputs
- generator run command
- output paths
- overwrite rules
- last generated timestamp

## Public contributor rule

A contributor should be able to answer:
> “If I edit this file, will the live site change?”

If the answer is unclear, the docs stack is still drifting.

---

*One site. One public truth path.*
