---
sidebar_position: 1
title: ActiveMirrorOS
---

# ActiveMirrorOS

**ActiveMirrorOS** is the operating system layer that brings MirrorDNA traces to life—managing runtime collection, storage, querying, and real-time monitoring of AI agent behavior.

## What is ActiveMirrorOS?

Think of ActiveMirrorOS as the **infrastructure layer** for observable AI:

- **Runtime**: Collects MirrorDNA traces as agents execute
- **Storage**: Efficiently stores and indexes traces
- **Query Engine**: Search and analyze trace data
- **APIs**: Programmatic access to traces
- **Monitoring**: Real-time dashboards and alerts

If MirrorDNA is the language, ActiveMirrorOS is the platform that speaks it.

## Key Features

### 1. Zero-Overhead Collection

Minimal performance impact through:
- Asynchronous trace writing
- Efficient serialization (CBOR, Protobuf)
- Batched I/O operations
- Smart buffering

**Typical overhead**: &lt;2% latency, &lt;5% memory

### 2. Scalable Storage

Handle millions of traces with:
- Time-series optimized storage
- Automatic compression (10:1 typical ratio)
- Retention policies
- Archive to cold storage

**Scales to**: Petabytes of traces

### 3. Powerful Queries

Find exactly what you need:
```sql
-- SQL-like query interface
SELECT * FROM traces
WHERE agent_id = 'support-bot'
  AND timestamp > '2024-01-01'
  AND events.semantics.intent = 'refund'
  AND events.semantics.confidence < 0.7
```

### 4. Real-Time Monitoring

Watch agents as they work:
- Live trace streaming
- Alert on anomalies
- Performance metrics
- Error tracking

### 5. Multi-Tenancy

Secure isolation for enterprise deployments:
- Namespace separation
- Role-based access control (RBAC)
- Encryption at rest and in transit
- Audit logging

## Architecture

```
┌─────────────────────────────────────┐
│         AI Agent Application        │
└──────────────┬──────────────────────┘
               │ MirrorDNA SDK
               ↓
┌─────────────────────────────────────┐
│      ActiveMirrorOS Runtime         │
│  ┌─────────────────────────────┐   │
│  │  Trace Collector            │   │
│  └─────────────────────────────┘   │
│  ┌─────────────────────────────┐   │
│  │  Event Buffer               │   │
│  └─────────────────────────────┘   │
│  ┌─────────────────────────────┐   │
│  │  Serializer & Compressor    │   │
│  └─────────────────────────────┘   │
└──────────────┬──────────────────────┘
               │
               ↓
┌─────────────────────────────────────┐
│      Storage Layer                  │
│  ┌──────────┐  ┌──────────────┐    │
│  │ Hot DB   │  │  Cold Archive│    │
│  │(TimeSeries)  │  (S3/Blob)  │    │
│  └──────────┘  └──────────────┘    │
└──────────────┬──────────────────────┘
               │
               ↓
┌─────────────────────────────────────┐
│      Query & Analytics Engine       │
│  • SQL Interface                    │
│  • Graph Queries                    │
│  • Aggregations                     │
│  • Streaming Analytics              │
└─────────────────────────────────────┘
```

## Components

### Trace Collector

Ingests MirrorDNA events from instrumented agents:
- HTTP/gRPC endpoints
- Language SDKs (Python, JavaScript, Go, Rust)
- Batch and streaming modes
- Schema validation

### Storage Engine

Time-series optimized storage:
- **Hot tier**: Recent traces (last 30 days) in fast DB
- **Warm tier**: Historical traces (30-180 days) compressed
- **Cold tier**: Archive (180+ days) in object storage

### Query API

Multiple query interfaces:
- **REST API**: HTTP/JSON for web apps
- **GraphQL**: Flexible queries for dashboards
- **SQL**: Powerful analytics with familiar syntax
- **gRPC**: High-performance for internal tools

### Monitoring Dashboard

Web UI for real-time observability:
- Trace explorer
- Agent performance metrics
- Error rates and trends
- Custom dashboards

## Getting Started

### Installation

```bash
# Docker (recommended for local development)
docker pull mirrordna/activemirror:latest
docker run -p 8080:8080 mirrordna/activemirror

# Kubernetes (production)
helm repo add mirrordna https://charts.mirrordna.org
helm install activemirror mirrordna/activemirror

# Binary (lightweight)
curl -fsSL https://get.activemirror.io | sh
activemirror start
```

### Configuration

```yaml
# activemirror.yaml
storage:
  type: postgres  # or clickhouse, timescaledb
  connection: postgresql://localhost/mirrordna
  
retention:
  hot_days: 30
  warm_days: 180
  cold_archive: s3://my-bucket/traces

query:
  max_results: 10000
  timeout: 30s

monitoring:
  port: 8080
  metrics_enabled: true
  tracing_enabled: true
```

### Instrument Your Agent

```python
from mirrordna import MirrorDNAClient

# Connect to ActiveMirrorOS
client = MirrorDNAClient(url="http://localhost:8080")

# Start a trace
with client.trace(agent_id="my-agent") as trace:
    trace.thought("User asked about pricing")
    trace.action("query_database", query="SELECT * FROM prices")
    trace.observation("Found 10 pricing tiers")
    trace.output("Our pricing starts at $9/month")
```

## Integration

ActiveMirrorOS integrates seamlessly with:

### Visualization
- **[Glyphtrail](/glyphtrail)**: Rich trace visualization
- **Grafana**: Time-series dashboards
- **Kibana**: Log analysis

### Compliance
- **[TrustByDesign](/trustbydesign)**: Automated compliance checks
- **Audit Export**: SOC2, GDPR, ISO reports

### Agents
- **[LingOS](/lingos)**: Built-in MirrorDNA support
- **LangChain**: Via callback integration
- **AutoGPT**: Plugin available

### Analytics
- **Jupyter**: Python SDK for analysis
- **Data warehouses**: Export to Snowflake, BigQuery
- **BI tools**: PowerBI, Tableau connectors

## Deployment Options

### 1. Cloud-Hosted (Managed)

Fully managed ActiveMirrorOS:
- Zero ops overhead
- Auto-scaling
- 99.9% SLA
- SOC2 compliant

**Best for**: Teams wanting plug-and-play

### 2. Self-Hosted (Docker/K8s)

Deploy in your infrastructure:
- Full control
- Data residency compliance
- Custom integrations
- Lower cost at scale

**Best for**: Enterprises with existing ops teams

### 3. Edge Deployment

Run locally on devices:
- Offline operation
- Privacy-first (no data leaves device)
- Low latency
- Embedded systems support

**Best for**: Edge AI, robotics, IoT

## Performance

Benchmarks (single node):

- **Ingestion**: 100K events/second
- **Query latency**: &lt;50ms (p99)
- **Storage**: 1M events ≈ 500MB compressed
- **Memory**: 2GB base + 100MB per 1M active traces

## Security

Built-in security features:

- **Authentication**: OAuth2, OIDC, API keys
- **Authorization**: RBAC, attribute-based access control
- **Encryption**: TLS 1.3, AES-256 at rest
- **Audit**: All API calls logged
- **Compliance**: GDPR, HIPAA, SOC2 ready

## Roadmap

Upcoming features:

- **Distributed tracing**: Cross-agent traces
- **Real-time analytics**: Stream processing
- **AI-powered insights**: Anomaly detection
- **Multi-region**: Global deployment
- **GraphQL subscriptions**: Live trace updates

## Community & Support

- **GitHub**: [ActiveMirrorOS](https://github.com/MirrorDNA-Reflection-Protocol/ActiveMirrorOS)
- **Docs**: [API Reference](https://docs.activemirror.io)
- **Discord**: Join the community
- **Support**: [support@mirrordna.org](mailto:support@mirrordna.org)

---

*The runtime for observable AI.* 🖥️
