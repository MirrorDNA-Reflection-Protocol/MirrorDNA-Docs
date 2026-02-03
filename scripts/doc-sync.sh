#!/bin/bash
# ⟡ MirrorDNA Doc Sync — Automated documentation updates
# Usage: ./scripts/doc-sync.sh [scan|sync|deploy|all]

set -e

DOCS_DIR="$HOME/repos/MirrorDNA-Docs"
SITE_DIR="$HOME/repos/activemirror-site"
TIMESTAMP=$(date +%Y-%m-%d)

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

echo -e "${CYAN}⟡ MirrorDNA Doc Sync${NC}"
echo "================================"

# ─────────────────────────────────────
# SCAN: Check what needs updating
# ─────────────────────────────────────
scan_repos() {
    echo -e "\n${YELLOW}Scanning repositories...${NC}"

    # Check activemirror-site version
    if [ -f "$SITE_DIR/package.json" ]; then
        SITE_VERSION=$(grep '"version"' "$SITE_DIR/package.json" | head -1 | sed 's/.*"version": "\(.*\)".*/\1/')
        echo "  activemirror-site: v$SITE_VERSION"
    fi

    # Check for recent changes
    if [ -d "$SITE_DIR/.git" ]; then
        echo "  Recent commits:"
        cd "$SITE_DIR" && git log --oneline -5 | sed 's/^/    /'
    fi

    # List pages
    echo -e "\n${YELLOW}Active Mirror Pages:${NC}"
    ls -1 "$SITE_DIR/src/pages/"*.jsx 2>/dev/null | xargs -n1 basename | sed 's/.jsx$//' | sed 's/^/  /'

    # Check docs
    echo -e "\n${YELLOW}Documentation Pages:${NC}"
    find "$DOCS_DIR" -name "index.html" -not -path "*/.git/*" | sed "s|$DOCS_DIR/||" | sed 's/index.html$//' | sed 's/^/  /'
}

# ─────────────────────────────────────
# SYNC: Extract info from code to docs
# ─────────────────────────────────────
sync_docs() {
    echo -e "\n${YELLOW}Syncing documentation...${NC}"

    # Extract version from site
    if [ -f "$SITE_DIR/package.json" ]; then
        SITE_VERSION=$(grep '"version"' "$SITE_DIR/package.json" | head -1 | sed 's/.*"version": "\(.*\)".*/\1/')
        echo "  Site version: $SITE_VERSION"
    fi

    # Count features
    PAGE_COUNT=$(ls -1 "$SITE_DIR/src/pages/"*.jsx 2>/dev/null | wc -l | tr -d ' ')
    COMPONENT_COUNT=$(ls -1 "$SITE_DIR/src/components/"*.jsx 2>/dev/null | wc -l | tr -d ' ')

    echo "  Pages: $PAGE_COUNT"
    echo "  Components: $COMPONENT_COUNT"

    # Generate changelog entry
    CHANGELOG_FILE="$DOCS_DIR/CHANGELOG.md"
    if [ ! -f "$CHANGELOG_FILE" ]; then
        echo "# MirrorDNA Documentation Changelog" > "$CHANGELOG_FILE"
        echo "" >> "$CHANGELOG_FILE"
    fi

    echo -e "\n${GREEN}✓ Sync complete${NC}"
}

# ─────────────────────────────────────
# DEPLOY: Push docs to GitHub Pages
# ─────────────────────────────────────
deploy_docs() {
    echo -e "\n${YELLOW}Deploying documentation...${NC}"

    cd "$DOCS_DIR"

    # Check for changes
    if [ -z "$(git status --porcelain)" ]; then
        echo "  No changes to deploy"
        return 0
    fi

    # Commit and push
    git add -A
    git commit -m "⟡ Doc sync — $TIMESTAMP — via doc-sync.sh"
    git push origin main

    echo -e "\n${GREEN}✓ Deployed to GitHub Pages${NC}"
    echo "  https://mirrordna-reflection-protocol.github.io/MirrorDNA-Docs/"
}

# ─────────────────────────────────────
# README AUDIT: Check all repo READMEs
# ─────────────────────────────────────
audit_readmes() {
    echo -e "\n${YELLOW}Auditing READMEs...${NC}"

    for repo in "$HOME/repos"/*/; do
        repo_name=$(basename "$repo")
        readme="$repo/README.md"

        if [ -f "$readme" ]; then
            lines=$(wc -l < "$readme" | tr -d ' ')
            last_modified=$(stat -f "%Sm" -t "%Y-%m-%d" "$readme" 2>/dev/null || echo "unknown")

            if [ "$lines" -lt 10 ]; then
                echo -e "  ${YELLOW}⚠${NC} $repo_name: $lines lines (sparse)"
            else
                echo -e "  ${GREEN}✓${NC} $repo_name: $lines lines"
            fi
        else
            echo -e "  ${YELLOW}⚠${NC} $repo_name: No README"
        fi
    done
}

# ─────────────────────────────────────
# MAIN
# ─────────────────────────────────────
case "${1:-all}" in
    scan)
        scan_repos
        ;;
    sync)
        sync_docs
        ;;
    deploy)
        deploy_docs
        ;;
    audit)
        audit_readmes
        ;;
    all)
        scan_repos
        sync_docs
        deploy_docs
        ;;
    *)
        echo "Usage: $0 [scan|sync|deploy|audit|all]"
        exit 1
        ;;
esac

echo -e "\n${CYAN}⟡ Done${NC}"
