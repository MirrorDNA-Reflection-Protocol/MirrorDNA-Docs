#!/usr/bin/env python3
"""
Check Markdown Links

Walks markdown files in this repo and checks relative links for likely breakage.
Prints a simple report of broken or suspicious links.
"""

import os
import re
from pathlib import Path
from urllib.parse import urlparse


def find_markdown_files(root_dir):
    """Find all markdown files in the repository."""
    markdown_files = []
    root_path = Path(root_dir)

    for md_file in root_path.rglob("*.md"):
        # Skip node_modules and other common directories
        if any(part in md_file.parts for part in ['.git', 'node_modules', 'build', 'dist', '.docusaurus']):
            continue
        markdown_files.append(md_file)

    return sorted(markdown_files)


def extract_links(file_path):
    """Extract all links from a markdown file."""
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    links = []

    # Markdown link pattern: [text](url)
    md_links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
    for text, url in md_links:
        links.append({
            'text': text,
            'url': url,
            'type': 'markdown',
            'line': None  # Could enhance to track line numbers
        })

    # HTML link pattern: <a href="url">
    html_links = re.findall(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>', content, re.IGNORECASE)
    for url in html_links:
        links.append({
            'text': '',
            'url': url,
            'type': 'html',
            'line': None
        })

    return links


def check_link(link, file_path, root_dir):
    """Check if a link is valid."""
    url = link['url']

    # Skip external URLs (http/https)
    if url.startswith(('http://', 'https://', 'mailto:', 'tel:')):
        return {'status': 'external', 'message': 'External link (not checked)'}

    # Skip anchors within the same page
    if url.startswith('#'):
        return {'status': 'anchor', 'message': 'Internal anchor (not checked)'}

    # Check relative file links
    if not url.startswith('/'):
        # Relative to current file
        target = file_path.parent / url.split('#')[0]  # Remove anchor
    else:
        # Relative to root
        target = root_dir / url.lstrip('/').split('#')[0]  # Remove anchor

    # Resolve the path
    try:
        target = target.resolve()
    except Exception as e:
        return {'status': 'error', 'message': f'Cannot resolve path: {e}'}

    # Check if file exists
    if not target.exists():
        return {'status': 'broken', 'message': f'File not found: {target}'}

    return {'status': 'ok', 'message': 'Link OK'}


def print_report(results):
    """Print a report of link checking results."""
    print("\n" + "=" * 110)
    print(" " * 35 + "MARKDOWN LINK CHECK REPORT")
    print("=" * 110 + "\n")

    total_files = len(results)
    total_links = sum(len(r['links']) for r in results)
    broken_links = sum(
        1 for r in results
        for link_result in r['link_results']
        if link_result['status'] == 'broken'
    )
    error_links = sum(
        1 for r in results
        for link_result in r['link_results']
        if link_result['status'] == 'error'
    )

    print(f"Scanned {total_files} markdown files")
    print(f"Found {total_links} links")
    print(f"Broken links: {broken_links}")
    print(f"Error links: {error_links}\n")

    if broken_links == 0 and error_links == 0:
        print("✅ All relative links are valid!\n")
        print("=" * 110 + "\n")
        return

    print("=" * 110)
    print("\n❌ Issues Found:\n")

    for result in results:
        file_path = result['file']
        has_issues = any(
            lr['status'] in ['broken', 'error']
            for lr in result['link_results']
        )

        if not has_issues:
            continue

        print(f"\nFile: {file_path}")
        print("-" * 110)

        for i, link_result in enumerate(result['link_results']):
            if link_result['status'] not in ['broken', 'error']:
                continue

            link = result['links'][i]
            status = link_result['status']
            message = link_result['message']

            status_emoji = "❌" if status == 'broken' else "⚠️"
            print(f"  {status_emoji} [{link['text']}]({link['url']})")
            print(f"     {message}")

    print("\n" + "=" * 110 + "\n")


def print_summary_table(results):
    """Print a summary table of link types."""
    # Count link types
    link_type_counts = {
        'ok': 0,
        'broken': 0,
        'error': 0,
        'external': 0,
        'anchor': 0
    }

    for result in results:
        for link_result in result['link_results']:
            status = link_result['status']
            link_type_counts[status] = link_type_counts.get(status, 0) + 1

    print("LINK BREAKDOWN")
    print("=" * 110)
    print(f"  ✅ Valid relative links:  {link_type_counts['ok']}")
    print(f"  ❌ Broken links:          {link_type_counts['broken']}")
    print(f"  ⚠️  Error links:           {link_type_counts['error']}")
    print(f"  🌐 External links:        {link_type_counts['external']} (not checked)")
    print(f"  🔗 Anchor links:          {link_type_counts['anchor']} (not checked)")
    print("=" * 110 + "\n")


def main():
    """Main entry point."""
    # Get the repository root (parent of tools directory)
    script_dir = Path(__file__).parent
    root_dir = script_dir.parent

    print(f"Checking markdown links in: {root_dir}\n")

    # Find all markdown files
    markdown_files = find_markdown_files(root_dir)

    if not markdown_files:
        print("No markdown files found!")
        return

    print(f"Found {len(markdown_files)} markdown files to check...")

    # Check links in each file
    results = []
    for md_file in markdown_files:
        links = extract_links(md_file)
        link_results = []

        for link in links:
            check_result = check_link(link, md_file, root_dir)
            link_results.append(check_result)

        results.append({
            'file': md_file.relative_to(root_dir),
            'links': links,
            'link_results': link_results
        })

    # Print report
    print_report(results)
    print_summary_table(results)

    # Exit with error code if broken links found
    broken_count = sum(
        1 for r in results
        for lr in r['link_results']
        if lr['status'] in ['broken', 'error']
    )

    if broken_count > 0:
        exit(1)


if __name__ == "__main__":
    main()
