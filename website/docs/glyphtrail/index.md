---
sidebar_position: 1
title: Glyphtrail
---

# Glyphtrail

**Glyphtrail** is an interactive timeline viewer for exploring MirrorDNA traces, visualizing agent decision-making processes with rich, intuitive interfaces.

## What is Glyphtrail?

Glyphtrail transforms raw MirrorDNA traces into beautiful, understandable visualizations:

- **Timeline View**: See events as they unfold
- **Graph View**: Understand relationships and dependencies
- **Diff View**: Compare traces side-by-side
- **Replay Mode**: Watch agents "think" in real-time
- **Search & Filter**: Find exactly what you need

## Key Features

### 1. Timeline Visualization

```
┌─────────────────────────────────────────────┐
│  Agent: customer-support-v1                 │
│  Session: sess_abc123                       │
│  Duration: 4.2s                             │
├─────────────────────────────────────────────┤
│                                             │
│  ●─────────────────────────────────────●   │
│  │         │         │         │       │   │
│  │         │         │         │       │   │
│  │    [thought]  [action]  [obs]   [output]│
│  │         │         │         │       │   │
│  │         ▼         ▼         ▼       ▼   │
│  │    "Classify  Query KB  Found 3  Send   │
│  │     intent"             results  reply" │
│  │         │         │         │       │   │
│  └─────────┴─────────┴─────────┴───────┘   │
│                                             │
│  Confidence:  ████████░░ 82%               │
│  PII Detected: No                           │
│  Tools Used: 2                              │
└─────────────────────────────────────────────┘
```

### 2. Interactive Event Details

Click any event to see:
- Full content
- Semantic annotations
- Confidence scores
- Privacy markers
- Tool parameters
- Timing information

### 3. Graph View

Visualize event relationships:

```
     [input]
        │
        ▼
    [thought] ──────┐
        │           │
        ▼           ▼
    [action]    [decision]
        │           │
        ▼           │
  [observation]     │
        │           │
        └─────┬─────┘
              ▼
          [output]
```

### 4. Trace Comparison

Compare two traces side-by-side:

```
┌─────────────────┬─────────────────┐
│   Version 1.0   │   Version 2.0   │
├─────────────────┼─────────────────┤
│ ● thought       │ ● thought       │
│ ● action (API)  │ ● action (API)  │
│ ● obs (success) │ ● obs (success) │
│ ● thought       │                 │ ← Removed
│ ● action (DB)   │ ● action (DB)   │
│ ● obs (3 items) │ ● obs (5 items) │ ← Difference
│ ● output        │ ● output        │
├─────────────────┼─────────────────┤
│ Duration: 5.2s  │ Duration: 3.8s  │ ← 27% faster
│ Confidence: 85% │ Confidence: 92% │ ← Improved
└─────────────────┴─────────────────┘
```

### 5. Replay Mode

Watch traces execute in real-time:

```
▶️ Play  ⏸️ Pause  ⏮️ Prev  ⏭️ Next  ⏩ Speed: 2x

┌─────────────────────────────────────┐
│  00:01.200 / 00:04.500             │
│  ████████████░░░░░░░░░░░░░░░░░░░  │
│                                     │
│  Current Event: action              │
│  ┌─────────────────────────────┐   │
│  │ Querying knowledge base...  │   │
│  │ Query: "refund policy"      │   │
│  │ Collection: "policies"      │   │
│  │ Status: In progress...      │   │
│  └─────────────────────────────┘   │
└─────────────────────────────────────┘
```

### 6. Search & Filter

Powerful query capabilities:

```
Search: [intent:refund AND confidence:<0.8]

Filters:
☑ Event Types: ☑ thought ☑ action ☑ observation ☐ error
☑ Time Range: Last 7 days
☑ Agent: customer-support-v1
☐ Contains PII
☑ Confidence: 0-100%
```

## Getting Started

### Installation

```bash
# Docker (standalone)
docker run -d \
  --name glyphtrail \
  -p 3000:3000 \
  -e ACTIVEMIRROR_URL=http://activemirror:8080 \
  mirrordna/glyphtrail:latest

# Access at http://localhost:3000
```

### With Docker Compose

```yaml
# docker-compose.yml
version: '3.8'

services:
  glyphtrail:
    image: mirrordna/glyphtrail:latest
    ports:
      - "3000:3000"
    environment:
      - ACTIVEMIRROR_URL=http://activemirror:8080
      - AUTH_ENABLED=true
      - AUTH_PROVIDER=oidc
    depends_on:
      - activemirror
```

### Configuration

```yaml
# glyphtrail.yaml
activemirror:
  url: http://activemirror:8080
  api_key: your-api-key

ui:
  theme: dark  # light, dark, auto
  default_view: timeline  # timeline, graph, table
  max_events_display: 1000
  
visualization:
  event_colors:
    thought: "#3498db"
    action: "#2ecc71"
    observation: "#f39c12"
    decision: "#9b59b6"
    output: "#1abc9c"
    error: "#e74c3c"
  
  show_confidence_bars: true
  show_timing_info: true
  animate_replay: true

export:
  formats: [pdf, png, json, csv]
  include_metadata: true
```

## Features in Detail

### Timeline View

**Best for**: Understanding sequential flow

Features:
- Chronological event display
- Event type icons
- Confidence indicators
- Duration bars
- Collapsible sections

**Use cases**:
- Debugging agent behavior
- Quality assurance reviews
- Customer support investigation

### Graph View

**Best for**: Understanding relationships

Features:
- Node-edge visualization
- Dependency arrows
- Event clustering
- Interactive navigation
- Export as DOT/GraphML

**Use cases**:
- Analyzing complex logic
- Finding bottlenecks
- Visualizing multi-agent systems

### Table View

**Best for**: Data analysis

Features:
- Sortable columns
- Filterable rows
- Export to CSV/Excel
- Bulk operations
- Statistical summaries

**Use cases**:
- Quantitative analysis
- Finding patterns
- Compliance reporting

### Diff View

**Best for**: Comparing versions

Features:
- Side-by-side comparison
- Highlighted differences
- Metric deltas
- A/B test results
- Version history

**Use cases**:
- Evaluating agent changes
- Testing improvements
- Regression detection

### Replay Mode

**Best for**: Step-by-step analysis

Features:
- Variable playback speed
- Pause at any point
- Step forward/backward
- Event annotations
- Export as video

**Use cases**:
- Training & education
- Demos & presentations
- Detailed debugging

## Advanced Features

### Annotations

Add notes to traces:

```javascript
// Add annotation
glyphtrail.annotate(trace_id, event_id, {
  author: "jane@company.com",
  text: "This is where the bug occurs",
  tags: ["bug", "investigate"],
  timestamp: Date.now()
});
```

### Collaborative Analysis

Share traces with team:

```
🔗 Share Link: https://glyphtrail.io/trace/550e8400...

Permissions:
☑ View  ☐ Comment  ☐ Edit  ☐ Export

Expires: 7 days  [Change ▼]
```

### Custom Visualizations

Create domain-specific views:

```javascript
import { createCustomView } from '@glyphtrail/sdk';

const medicalView = createCustomView({
  name: "Clinical Decision View",
  layout: "hierarchical",
  eventRenderer: (event) => {
    if (event.semantics.medical) {
      return <MedicalEventCard event={event} />;
    }
    return <DefaultEventCard event={event} />;
  },
  filters: ["medical_only"]
});

glyphtrail.registerView(medicalView);
```

### Analytics Dashboard

Aggregate insights across traces:

```
┌─────────────────────────────────────┐
│  Agent Performance (Last 30 Days)   │
├─────────────────────────────────────┤
│  Total Traces: 12,450               │
│  Avg Duration: 3.2s                 │
│  Avg Confidence: 87%                │
│  Error Rate: 2.1%                   │
│                                     │
│  Top Intents:                       │
│  ██████████████ refund (34%)        │
│  ████████ shipping (21%)            │
│  ██████ product_info (15%)          │
│                                     │
│  Confidence Over Time:              │
│  ▁▂▃▅▆▇█▇▆▅▄▃▂▁                    │
└─────────────────────────────────────┘
```

## Integration

### Embed in Your App

```html
<!-- Embed Glyphtrail widget -->
<iframe
  src="https://glyphtrail.io/embed/trace/550e8400..."
  width="100%"
  height="600"
  frameborder="0">
</iframe>
```

### API Access

```javascript
import GlyphtrailClient from '@glyphtrail/client';

const client = new GlyphtrailClient({
  url: 'https://glyphtrail.io',
  apiKey: 'your-api-key'
});

// Load trace
const trace = await client.getTrace('550e8400...');

// Render to canvas
client.render(trace, {
  container: document.getElementById('trace-view'),
  view: 'timeline',
  theme: 'dark'
});
```

### Export Options

Export traces in multiple formats:

- **PDF**: Printable reports
- **PNG/SVG**: Image exports
- **JSON**: Raw data
- **CSV**: Tabular export
- **Video**: MP4 replay recordings

## Use Cases

### 1. Debugging

Identify where agent logic failed:
- See exact event sequence
- Check confidence scores
- Inspect tool parameters
- Find error sources

### 2. Quality Assurance

Review agent interactions:
- Audit sample traces
- Verify compliance
- Check response quality
- Identify edge cases

### 3. Training & Education

Teach how agents work:
- Show decision-making process
- Explain AI reasoning
- Demonstrate best practices
- Create training materials

### 4. Customer Support

Investigate user issues:
- Replay user sessions
- Understand agent responses
- Find resolution paths
- Improve future interactions

### 5. Research

Study AI behavior:
- Analyze decision patterns
- Compare strategies
- Test hypotheses
- Publish findings

## Performance

- **Load time**: &lt;2s for traces up to 10K events
- **Rendering**: 60 FPS smooth scrolling
- **Search**: &lt;100ms for indexed queries
- **Export**: Real-time streaming for large traces

## Security

- **Authentication**: OAuth2, SAML, API keys
- **Authorization**: Trace-level access control
- **Encryption**: TLS 1.3 in transit
- **Privacy**: PII redaction in UI
- **Audit**: All views and exports logged

## Roadmap

Coming soon:

- **Real-time collaboration**: Multi-user trace analysis
- **AI-powered insights**: Auto-detect anomalies
- **3D visualization**: Complex multi-agent systems
- **Mobile app**: iOS and Android viewers
- **Voice annotations**: Speak notes while reviewing

## Resources

- **GitHub**: [Glyphtrail](https://github.com/MirrorDNA-Reflection-Protocol/Glyphtrail)
- **Live Demo**: [Try Glyphtrail](https://demo.glyphtrail.io)
- **Docs**: [User guide](https://docs.glyphtrail.io)
- **Gallery**: [Example visualizations](https://gallery.glyphtrail.io)

---

*Visualize AI thinking.* 📊
