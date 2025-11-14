#!/usr/bin/env python3
"""
Print MirrorDNA Ecosystem Map

Reads ecosystem_map.json and displays:
- A nice table grouped by role
- Simple counts (public vs private)
"""

import json
import os
from collections import defaultdict
from pathlib import Path


def load_ecosystem_map():
    """Load the ecosystem map JSON file."""
    script_dir = Path(__file__).parent
    map_file = script_dir / "ecosystem_map.json"

    if not map_file.exists():
        print(f"Error: {map_file} not found!")
        exit(1)

    with open(map_file, 'r') as f:
        return json.load(f)


def print_table_header():
    """Print table header."""
    print(f"{'Repository':<35} {'Visibility':<12} {'Description':<60}")
    print("=" * 110)


def print_repo_row(repo):
    """Print a single repository row."""
    name = repo['name']
    visibility = repo['visibility']
    desc = repo['description']

    # Truncate description if too long
    if len(desc) > 60:
        desc = desc[:57] + "..."

    # Add emoji for visibility
    vis_emoji = "🌐" if visibility == "public" else "🔒"
    visibility_str = f"{vis_emoji} {visibility}"

    print(f"{name:<35} {visibility_str:<12} {desc:<60}")


def print_ecosystem(data):
    """Print ecosystem map grouped by role."""
    repos = data['repositories']

    # Group by role
    by_role = defaultdict(list)
    for repo in repos:
        by_role[repo['role']].append(repo)

    # Role order and display names
    role_info = {
        'spec': ('📋 Specification', '━'),
        'docs': ('📚 Documentation', '━'),
        'product': ('🚀 Products', '━'),
        'sdk': ('🔧 SDKs', '━'),
        'playground': ('🎮 Playground', '━'),
        'r&d': ('🔬 R&D', '━')
    }

    print("\n" + "=" * 110)
    print(" " * 35 + "MIRRORDNA ECOSYSTEM MAP")
    print("=" * 110 + "\n")

    # Print each role group
    for role_key in ['spec', 'docs', 'product', 'sdk', 'playground', 'r&d']:
        if role_key not in by_role:
            continue

        role_name, separator = role_info[role_key]
        repos_in_role = by_role[role_key]

        print(f"\n{role_name}")
        print(separator * 110)
        print_table_header()

        for repo in sorted(repos_in_role, key=lambda x: x['name']):
            print_repo_row(repo)

    print("\n" + "=" * 110 + "\n")


def print_summary(data):
    """Print summary statistics."""
    repos = data['repositories']

    # Count by visibility
    public_count = sum(1 for r in repos if r['visibility'] == 'public')
    private_count = sum(1 for r in repos if r['visibility'] == 'private')

    # Count by role
    role_counts = defaultdict(int)
    for repo in repos:
        role_counts[repo['role']] += 1

    print("SUMMARY")
    print("=" * 110)
    print(f"\nTotal repositories: {len(repos)}")
    print(f"  🌐 Public:  {public_count}")
    print(f"  🔒 Private: {private_count}")

    print(f"\nBy role:")
    role_names = {
        'spec': 'Specifications',
        'docs': 'Documentation',
        'product': 'Products',
        'sdk': 'SDKs',
        'playground': 'Playground/Examples',
        'r&d': 'Research & Development'
    }

    for role_key in ['spec', 'docs', 'product', 'sdk', 'playground', 'r&d']:
        if role_key in role_counts:
            role_name = role_names.get(role_key, role_key)
            count = role_counts[role_key]
            print(f"  {role_name:<25}: {count}")

    print("\n" + "=" * 110 + "\n")


def main():
    """Main entry point."""
    try:
        data = load_ecosystem_map()
        print_ecosystem(data)
        print_summary(data)
    except Exception as e:
        print(f"Error: {e}")
        exit(1)


if __name__ == "__main__":
    main()
