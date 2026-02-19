#!/usr/bin/env python3
"""
⟡ MirrorDNA Doc Generator — Reads SHIPLOG.md → Updates MirrorDNA-Docs HTML pages.
Run: python3 scripts/generate_docs.py
"""

import re
import os
from pathlib import Path
from datetime import datetime, date

SHIPLOG = Path.home() / ".mirrordna" / "SHIPLOG.md"
INFRA = Path.home() / ".mirrordna" / "INFRASTRUCTURE.md"
DOCS_DIR = Path.home() / "repos" / "MirrorDNA-Docs"

# ─── Parse SHIPLOG ────────────────────────────────────────────────────────────

def parse_shiplog():
    """Parse SHIPLOG.md into structured data."""
    text = SHIPLOG.read_text()
    sections = {}
    current_section = None
    current_module = None
    items = []

    for line in text.split('\n'):
        if line.startswith('## '):
            if current_section and items:
                sections[current_section] = {'module': current_module, 'items': items}
            current_section = line[3:].strip()
            current_module = None
            items = []
        elif line.startswith('> Module:'):
            current_module = line.split('`')[1] if '`' in line else line
        elif line.startswith('- **'):
            # Extract: name, description, date — handle both — and : separators
            m = re.match(r'- \*\*(.+?)\*\*\s*(?:\([^)]*\))?\s*[—:]\s*(.+?)(?:\s*`SHIPPED (\d{4}-\d{2}-\d{2})`)?$', line)
            if m:
                items.append({
                    'name': m.group(1),
                    'desc': m.group(2).strip().rstrip('`').strip(),
                    'date': m.group(3) or 'unknown',
                })
        elif line.startswith('- Location:') or line.startswith('- Spec:') or line.startswith('- SHIPPED:'):
            # Metadata lines for section-level items
            if items and line.startswith('- SHIPPED:'):
                d = re.search(r'(\d{4}-\d{2}-\d{2})', line)
                if d and items[-1]['date'] == 'unknown':
                    items[-1]['date'] = d.group(1)

    if current_section and items:
        sections[current_section] = {'module': current_module, 'items': items}

    return sections


def get_ship_dates(sections):
    """Get all ship dates for timeline."""
    dates = {}
    for section, data in sections.items():
        for item in data['items']:
            d = item['date']
            if d != 'unknown':
                dates.setdefault(d, []).append({'section': section, **item})
    return dict(sorted(dates.items()))


def count_ships(sections):
    total = sum(len(d['items']) for d in sections.values())
    return total


# ─── HTML Template Helpers ────────────────────────────────────────────────────

NAV_TEMPLATE = '''    <nav class="nav">
        <div class="nav-inner">
            <a href="./" class="nav-logo">
                <span class="nav-logo-glyph">⟡</span>
                <span class="nav-logo-text">MirrorDNA</span>
            </a>
            <button class="nav-mobile-toggle"
                onclick="document.querySelector('.nav-links').classList.toggle('open')">☰</button>
            <ul class="nav-links">
                <li><a href="story/"{story_active}>Story</a></li>
                <li><a href="principles/"{principles_active}>Principles</a></li>
                <li><a href="architecture/"{architecture_active}>Architecture</a></li>
                <li><a href="security/"{security_active}>Security</a></li>
                <li><a href="capabilities/"{capabilities_active}>Capabilities</a></li>
                <li><a href="activemirror/" style="color: #a855f7;"{activemirror_active}>Active Mirror</a></li>
                <li><a href="research/"{research_active}>Research</a></li>
                <li><a href="ecosystem/"{ecosystem_active}>Ecosystem</a></li>
            </ul>
        </div>
    </nav>'''

def nav(active=''):
    pages = ['story','principles','architecture','security','capabilities','activemirror','research','ecosystem']
    attrs = {}
    for p in pages:
        attrs[f'{p}_active'] = ' class="active"' if p == active else ''
    return NAV_TEMPLATE.format(**attrs)


HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <base href="/MirrorDNA-Docs/">
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
    <link rel="icon" type="image/svg+xml" href="favicon.svg">
</head>'''

FOOTER = '''
    <footer class="footer">
        <div class="container">
            <p>⟡ MirrorDNA — Sovereign AI Infrastructure</p>
            <p style="margin-top: 0.5rem; color: var(--text-muted); font-size: 0.8rem;">
                N1 Intelligence · {year} · Auto-generated from SHIPLOG on {date}
            </p>
        </div>
    </footer>
</main>
</body>
</html>'''

def footer():
    return FOOTER.format(year=date.today().year, date=date.today().isoformat())


def capability_card(name, desc, icon='⟡'):
    return f'''                <div class="capability-card">
                    <div class="capability-header">
                        <span class="capability-icon">{icon}</span>
                        <h4>{name}</h4>
                    </div>
                    <p>{desc}</p>
                </div>'''


# ─── Generate Capabilities Page ───────────────────────────────────────────────

def generate_capabilities(sections):
    total = count_ships(sections)

    # Group by category — covers ALL SHIPLOG sections
    categories = {
        'Security & Safety': {
            'icon': '🛡️',
            'desc': 'Defense-in-depth architecture. Kavach scam shield. Chetana deepfake detection. Fail-closed by default.',
            'sections': ['Kavach', 'Kavach / Chetana', 'Kavach/Chetana'],
        },
        'Intelligence & Inference': {
            'icon': '◈',
            'desc': 'Multi-model orchestration with sovereign routing. Swarm intelligence. Research monitoring.',
            'sections': ['MirrorSwarm Orchestration Engine', 'MirrorSwarm Terminal Spawner', 'Intelligence'],
        },
        'Memory & Identity': {
            'icon': '⧉',
            'desc': 'Persistent state across sessions. Memory lifecycle. Vault integrity. Continuity bus.',
            'sections': ['Continuity System (this file)', 'Vault Organization'],
        },
        'Consumer Products': {
            'icon': '⟡',
            'desc': 'User-facing products built on sovereign infrastructure.',
            'sections': ['ActiveMirror Site', 'Active Mirror Site', 'ActiveMirrorOS'],
        },
        'Infrastructure & Automation': {
            'icon': '⚙',
            'desc': 'Self-healing infrastructure. 24 managed services. Phone sync. Domain monitoring. Auto-backup.',
            'sections': ['Factory Trigger', 'Cognitive Dashboard', 'Dashboard', 'INFRASTRUCTURE',
                         'Infrastructure', 'MirrorDNA Infrastructure', 'Swarm Automation'],
        },
        'Publishing & Distribution': {
            'icon': '📡',
            'desc': 'Multi-platform publishing. Auto-synthesized beacon. 6 distribution channels.',
            'sections': ['MirrorPublish', 'MirrorPublish Content', 'Beacon Auto-Publish', 'Publications', 'MirrorRadar'],
        },
        'Sovereign Factory': {
            'icon': '🏭',
            'desc': 'Multi-agent manufacturing pipeline. Voice-triggered. BenQ grid visualization.',
            'sections': ['Sovereign Factory', 'Swarm Choreography Pattern'],
        },
    }

    cards_html = ''
    for cat_name, cat in categories.items():
        items = []
        for sec_name in cat['sections']:
            if sec_name in sections:
                items.extend(sections[sec_name]['items'])

        if not items:
            continue

        cards = '\n'.join(capability_card(it['name'], it['desc']) for it in items[:12])  # cap at 12 per category

        cards_html += f'''
            <h2 id="{cat_name.lower().replace(' ', '-').replace('&', 'and')}">{cat['icon']} {cat_name}</h2>
            <p>{cat['desc']}</p>
            <p style="color: var(--text-muted); font-size: 0.85rem;">{len(items)} shipped capabilities</p>

            <div class="capability-grid">
{cards}
            </div>
'''

    html = f'''{HEAD.format(title="System Capabilities — What MirrorDNA Can Do", desc=f"{total} shipped capabilities across security, intelligence, memory, infrastructure, and consumer products.")}

<body>
{nav('capabilities')}

    <main>
        <div class="container">
            <p class="subtitle">System Capabilities</p>
            <h1>What MirrorDNA Can Do</h1>

            <p class="lead">
                <strong>{total} shipped capabilities</strong> across seven layers. Each component is tested, documented, and running daily on dedicated hardware.
            </p>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); gap: 1rem; margin: 2rem 0;">
                <div style="text-align: center; padding: 1rem; background: var(--bg-card); border-radius: 1rem; border: 1px solid var(--border-subtle);">
                    <div style="font-size: 1.5rem; font-weight: 700; color: var(--accent-primary);">{total}</div>
                    <div style="font-size: 0.75rem; color: var(--text-muted);">Shipped</div>
                </div>
                <div style="text-align: center; padding: 1rem; background: var(--bg-card); border-radius: 1rem; border: 1px solid var(--border-subtle);">
                    <div style="font-size: 1.5rem; font-weight: 700; color: var(--accent-primary);">{len(categories)}</div>
                    <div style="font-size: 0.75rem; color: var(--text-muted);">Layers</div>
                </div>
                <div style="text-align: center; padding: 1rem; background: var(--bg-card); border-radius: 1rem; border: 1px solid var(--border-subtle);">
                    <div style="font-size: 1.5rem; font-weight: 700; color: var(--accent-primary);">{len(sections)}</div>
                    <div style="font-size: 0.75rem; color: var(--text-muted);">Systems</div>
                </div>
            </div>

{cards_html}
        </div>
{footer()}'''

    (DOCS_DIR / 'capabilities' / 'index.html').write_text(html)
    print(f'  ✓ capabilities/ — {total} capabilities across {len(categories)} categories')


# ─── Generate Story/Timeline Page ─────────────────────────────────────────────

def generate_story(sections):
    dates = get_ship_dates(sections)

    timeline_html = ''
    for d, items in reversed(list(dates.items())):
        items_html = '\n'.join(
            f'                    <li><strong>{it["name"]}</strong> ({it["section"]}) — {it["desc"][:100]}</li>'
            for it in items[:8]  # cap per day
        )
        more = f' <li style="color: var(--text-muted);">...and {len(items)-8} more</li>' if len(items) > 8 else ''

        timeline_html += f'''
            <div class="timeline-item">
                <div class="timeline-date">{d}</div>
                <div class="timeline-content">
                    <p style="color: var(--text-muted); font-size: 0.85rem;">{len(items)} ships</p>
                    <ul style="list-style: none; padding: 0;">
{items_html}{more}
                    </ul>
                </div>
            </div>'''

    total = count_ships(sections)
    first_date = min(dates.keys()) if dates else '2025-04'
    last_date = max(dates.keys()) if dates else date.today().isoformat()

    html = f'''{HEAD.format(title="Story — How MirrorDNA Got Here", desc="Timeline of MirrorDNA development from April 2025 to present.")}

<body>
{nav('story')}

    <main>
        <div class="container">
            <p class="subtitle">Origin & Timeline</p>
            <h1>How MirrorDNA Got Here</h1>

            <p class="lead">
                Started April 2025. One person. No funding. No team. Just a question:
                <em>What does a company look like when the founder is the only human?</em>
            </p>

            <p class="lead" style="color: var(--text-muted); font-size: 1rem;">
                {total} capabilities shipped. {len(dates)} active development days tracked. Latest ship: {last_date}.
            </p>

            <h2>Ship Timeline</h2>
            <p>Every line below is a shipped, running capability — not a plan or a prototype.</p>

            <div class="timeline">
{timeline_html}
            </div>
        </div>
{footer()}'''

    (DOCS_DIR / 'story' / 'index.html').write_text(html)
    print(f'  ✓ story/ — {len(dates)} days, {total} ships')


# ─── Generate Security Page ──────────────────────────────────────────────────

def generate_security(sections):
    kavach_items = []
    for key in ['Kavach', 'Kavach / Chetana', 'Kavach/Chetana']:
        if key in sections:
            kavach_items.extend(sections[key]['items'])

    kavach_cards = '\n'.join(capability_card(it['name'], it['desc'], '⛨') for it in kavach_items)

    # Infrastructure security
    infra_items = []
    for key in ['Infrastructure', 'MirrorDNA Infrastructure']:
        if key in sections:
            infra_items.extend([it for it in sections[key]['items'] if any(w in it['name'].lower() for w in ['security', 'audit', 'snapshot', 'dns', 'heal'])])

    infra_cards = '\n'.join(capability_card(it['name'], it['desc'], '🔒') for it in infra_items)

    html = f'''{HEAD.format(title="Security Architecture — MirrorDNA", desc="Defense-in-depth security: AMGL Guard, MirrorGate, Kavach AI Shield, red-team testing.")}

<body>
{nav('security')}

    <main>
        <div class="container">
            <p class="subtitle">Security Architecture</p>
            <h1>Defense in Depth</h1>

            <p class="lead">
                Security is not a layer — it's the foundation. Every component fails closed. Every action is auditable.
                Every model is governed.
            </p>

            <h2 id="amgl">⟡ AMGL Guard</h2>
            <p>Pre-inference policy enforcement. 23 rules in ActiveMirrorOS. Blocks prompt exfiltration, role injection, social engineering, jailbreaks.</p>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin: 1.5rem 0;">
                <div style="text-align: center; padding: 1.5rem; background: var(--bg-card); border-radius: 1rem; border: 1px solid rgba(99,102,241,0.2);">
                    <div style="font-size: 2rem; font-weight: 700; color: var(--accent-primary);">23</div>
                    <div style="font-size: 0.8rem; color: var(--text-muted);">Guard Rules</div>
                </div>
                <div style="text-align: center; padding: 1.5rem; background: var(--bg-card); border-radius: 1rem; border: 1px solid rgba(16,185,129,0.2);">
                    <div style="font-size: 2rem; font-weight: 700; color: var(--accent-success);">12,096</div>
                    <div style="font-size: 0.8rem; color: var(--text-muted);">Lines in Control Plane</div>
                </div>
                <div style="text-align: center; padding: 1.5rem; background: var(--bg-card); border-radius: 1rem; border: 1px solid rgba(245,158,11,0.2);">
                    <div style="font-size: 2rem; font-weight: 700; color: var(--accent-warning);">Fail-Closed</div>
                    <div style="font-size: 0.8rem; color: var(--text-muted);">Default Behavior</div>
                </div>
            </div>

            <h2 id="mirrorgate">🔒 MirrorGate</h2>
            <p>Application-layer safety proxy. Real-time safety scoring. Sits between user and model — every request is evaluated before inference begins.</p>

            <h2 id="kavach">⛨ Kavach — Sovereign AI Shield</h2>
            <p>Consumer-facing scam detection and digital safety for India. {len(kavach_items)} shipped capabilities including deepfake detection, voice clone analysis, QR code scanning, and SMS auto-scanning.</p>

            <div class="capability-grid">
{kavach_cards}
            </div>

            <h2 id="infrastructure-security">🔐 Infrastructure Security</h2>
            <p>System-level security hardening, monitoring, and self-healing.</p>

            <div class="capability-grid">
{infra_cards}
            </div>

            <h2 id="red-team">🎯 Red-Team Testing</h2>
            <p>175 attacks tested across 5 categories (December 2025). Prompt exfiltration, role injection, meta-instruction, social engineering, jailbreak patterns. Vulnerabilities found, patched, verified.</p>
        </div>
{footer()}'''

    (DOCS_DIR / 'security' / 'index.html').write_text(html)
    print(f'  ✓ security/ — AMGL + MirrorGate + {len(kavach_items)} Kavach capabilities')


# ─── Generate Homepage ────────────────────────────────────────────────────────

def generate_homepage(sections):
    total = count_ships(sections)
    dates = get_ship_dates(sections)
    latest = max(dates.keys()) if dates else date.today().isoformat()

    html = f'''{HEAD.format(title="MirrorDNA — Sovereign AI Infrastructure", desc=f"Sovereign AI infrastructure. {total} shipped capabilities. 95 repos. 9 layers. Built by one person.")}

<body>
{nav()}

    <main>
        <div class="container">
            <div class="hero">
                <p class="subtitle">Sovereign AI Infrastructure</p>
                <h1>⟡ MirrorDNA</h1>
                <p class="lead">
                    What does a company look like when the founder is the only human and the entire operation runs on
                    orchestrated AI?
                </p>
                <p class="lead" style="color: var(--text-muted); font-size: 1rem;">
                    95 repositories. 9 architectural layers. {total} shipped capabilities. One person. No funding. Running in production.
                </p>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 1rem; margin: 2rem 0;">
                <div style="text-align: center; padding: 1.25rem; background: var(--bg-card); border-radius: 1rem; border: 1px solid var(--border-subtle);">
                    <div style="font-size: 1.75rem; font-weight: 700; color: var(--accent-primary);">95</div>
                    <div style="font-size: 0.75rem; color: var(--text-muted);">Repos</div>
                </div>
                <div style="text-align: center; padding: 1.25rem; background: var(--bg-card); border-radius: 1rem; border: 1px solid var(--border-subtle);">
                    <div style="font-size: 1.75rem; font-weight: 700; color: var(--accent-primary);">9</div>
                    <div style="font-size: 0.75rem; color: var(--text-muted);">Layers</div>
                </div>
                <div style="text-align: center; padding: 1.25rem; background: var(--bg-card); border-radius: 1rem; border: 1px solid var(--border-subtle);">
                    <div style="font-size: 1.75rem; font-weight: 700; color: var(--accent-primary);">{total}</div>
                    <div style="font-size: 0.75rem; color: var(--text-muted);">Shipped</div>
                </div>
                <div style="text-align: center; padding: 1.25rem; background: var(--bg-card); border-radius: 1rem; border: 1px solid var(--border-subtle);">
                    <div style="font-size: 1.75rem; font-weight: 700; color: var(--accent-success);">63</div>
                    <div style="font-size: 0.75rem; color: var(--text-muted);">Public</div>
                </div>
            </div>

            <h2>Core Systems</h2>
            <div class="capability-grid">
                <a href="activemirror/" style="text-decoration: none;">
                    <div class="capability-card" style="cursor: pointer;">
                        <div class="capability-header"><span class="capability-icon">⟡</span><h4>Active Mirror</h4></div>
                        <p>Reflective AI — asks questions to help you think. BrainScan, AI Twins, Sovereign Mode.</p>
                    </div>
                </a>
                <a href="security/#kavach" style="text-decoration: none;">
                    <div class="capability-card" style="cursor: pointer;">
                        <div class="capability-header"><span class="capability-icon">⛨</span><h4>Kavach</h4></div>
                        <p>Sovereign AI shield for India. Scam detection, deepfakes, voice clones, QR scanning, SMS auto-scan.</p>
                    </div>
                </a>
                <a href="capabilities/" style="text-decoration: none;">
                    <div class="capability-card" style="cursor: pointer;">
                        <div class="capability-header"><span class="capability-icon">◈</span><h4>MirrorBrain</h4></div>
                        <p>Cognitive interface — 12-screen mobile app with Pulse, Ask, Vault, Galaxy graph, mesh chat.</p>
                    </div>
                </a>
                <a href="architecture/" style="text-decoration: none;">
                    <div class="capability-card" style="cursor: pointer;">
                        <div class="capability-header"><span class="capability-icon">⧉</span><h4>ActiveMirrorOS</h4></div>
                        <p>Control plane — 12,096 lines. Identity kernel, AMGL guard, vault lineage, consent ledger.</p>
                    </div>
                </a>
            </div>

            <h2>Explore</h2>
            <div class="capability-grid">
                <a href="story/" style="text-decoration: none;"><div class="capability-card" style="cursor: pointer;"><h4>Story →</h4><p>10 months. How it all started.</p></div></a>
                <a href="principles/" style="text-decoration: none;"><div class="capability-card" style="cursor: pointer;"><h4>Principles →</h4><p>Truth-State Law. Zero Drift. Vault Supremacy.</p></div></a>
                <a href="security/" style="text-decoration: none;"><div class="capability-card" style="cursor: pointer;"><h4>Security →</h4><p>AMGL Guard. MirrorGate. Red-team tested.</p></div></a>
                <a href="ecosystem/" style="text-decoration: none;"><div class="capability-card" style="cursor: pointer;"><h4>Ecosystem →</h4><p>Interactive map of 95 repositories.</p></div></a>
                <a href="research/" style="text-decoration: none;"><div class="capability-card" style="cursor: pointer;"><h4>Research →</h4><p>SCD Protocol. Published papers.</p></div></a>
                <a href="https://activemirror.ai" style="text-decoration: none;"><div class="capability-card" style="cursor: pointer; border-color: rgba(168,85,247,0.3);"><h4>activemirror.ai →</h4><p>Try the live system.</p></div></a>
            </div>

            <p style="text-align: center; color: var(--text-muted); margin-top: 3rem; font-size: 0.85rem;">
                Last updated: {latest} · Auto-generated from SHIPLOG
            </p>
        </div>
{footer()}'''

    (DOCS_DIR / 'index.html').write_text(html)
    print(f'  ✓ index.html — {total} ships, latest {latest}')


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    print('⟡ MirrorDNA Doc Generator')
    print(f'  Reading: {SHIPLOG}')

    if not SHIPLOG.exists():
        print('  ERROR: SHIPLOG.md not found')
        return

    sections = parse_shiplog()
    total = count_ships(sections)
    print(f'  Parsed: {len(sections)} sections, {total} capabilities')
    print()

    # Generate pages
    generate_homepage(sections)
    generate_capabilities(sections)
    generate_story(sections)
    generate_security(sections)

    print(f'\n⟡ Done — {4} pages updated')
    print(f'  Deploy: cd {DOCS_DIR} && git add -A && git commit -m "doc-gen: {date.today()}" && git push')


if __name__ == '__main__':
    main()
