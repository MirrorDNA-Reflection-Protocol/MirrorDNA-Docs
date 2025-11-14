---
sidebar_position: 2
title: Getting Started
---

# Getting Started with ActiveMirrorOS

This guide will get you up and running with ActiveMirrorOS in minutes.

## Prerequisites

- Docker (for local development) OR
- Kubernetes cluster (for production) OR
- Linux/macOS system (for binary installation)

## Quick Start (Docker)

The fastest way to try ActiveMirrorOS:

```bash
# Pull and run ActiveMirrorOS
docker run -d \
  --name activemirror \
  -p 8080:8080 \
  -p 9090:9090 \
  -v activemirror-data:/data \
  mirrordna/activemirror:latest

# Verify it's running
curl http://localhost:8080/health
# Should return: {"status": "healthy"}
```

Access the dashboard at: http://localhost:8080

## Installation Options

### Option 1: Docker Compose (Recommended for Development)

```yaml
# docker-compose.yml
version: '3.8'

services:
  activemirror:
    image: mirrordna/activemirror:latest
    ports:
      - "8080:8080"  # HTTP API
      - "9090:9090"  # Metrics
    environment:
      - STORAGE_TYPE=postgres
      - DATABASE_URL=postgresql://postgres:password@db:5432/mirrordna
    volumes:
      - ./config:/etc/activemirror
    depends_on:
      - db
  
  db:
    image: timescale/timescaledb:latest-pg14
    environment:
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=mirrordna
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

```bash
docker-compose up -d
```

### Option 2: Kubernetes (Production)

```bash
# Add Helm repo
helm repo add mirrordna https://charts.mirrordna.org
helm repo update

# Install with default values
helm install activemirror mirrordna/activemirror

# Or with custom values
helm install activemirror mirrordna/activemirror \
  --set storage.type=postgres \
  --set storage.connectionString="postgresql://..." \
  --set replicaCount=3
```

### Option 3: Binary Install

```bash
# Download and install
curl -fsSL https://get.activemirror.io | sh

# Start ActiveMirrorOS
activemirror start --config activemirror.yaml
```

## Configuration

Create `activemirror.yaml`:

```yaml
# Server configuration
server:
  host: 0.0.0.0
  port: 8080
  read_timeout: 30s
  write_timeout: 30s

# Storage backend
storage:
  type: postgres  # postgres, clickhouse, timescaledb
  connection: postgresql://localhost:5432/mirrordna
  pool_size: 20
  
# Retention policies
retention:
  hot_tier_days: 30      # Fast access
  warm_tier_days: 180    # Compressed
  cold_archive_enabled: true
  cold_archive_url: s3://my-bucket/traces

# Query limits
query:
  max_results: 10000
  default_limit: 100
  timeout: 30s
  max_concurrent: 50

# Monitoring
monitoring:
  enabled: true
  metrics_port: 9090
  health_check_interval: 10s

# Security
security:
  auth_enabled: true
  auth_type: oidc  # oidc, api_key, none
  oidc_issuer: https://auth.example.com
  
# Logging
logging:
  level: info  # debug, info, warn, error
  format: json
```

## Instrumenting Your First Agent

### Python Example

```python
# Install SDK
pip install mirrordna-sdk

# Instrument your agent
from mirrordna import MirrorDNAClient

# Initialize client
client = MirrorDNAClient(
    url="http://localhost:8080",
    api_key="your-api-key"  # Optional if auth disabled
)

# Create a traced agent function
def customer_support_agent(user_message):
    with client.trace(
        agent_id="support-agent-v1",
        session_id="sess_123"
    ) as trace:
        # Log thought process
        trace.thought(f"User asked: {user_message}")
        
        # Classify intent
        intent = classify_intent(user_message)
        trace.decision("intent_classification", {
            "intent": intent,
            "confidence": 0.92
        })
        
        # Take action
        trace.action("query_knowledge_base", {
            "query": user_message,
            "intent": intent
        })
        
        # Get results
        results = search_kb(user_message)
        trace.observation(f"Found {len(results)} results")
        
        # Generate response
        response = generate_response(results)
        trace.output(response, {
            "citations": [r["id"] for r in results]
        })
        
        return response

# Use it
response = customer_support_agent("How do I reset my password?")
```

### JavaScript/TypeScript Example

```typescript
// Install SDK
npm install @mirrordna/sdk

// Instrument your agent
import { MirrorDNAClient } from '@mirrordna/sdk';

const client = new MirrorDNAClient({
  url: 'http://localhost:8080',
  apiKey: 'your-api-key'
});

async function chatAgent(userMessage: string) {
  const trace = await client.startTrace({
    agentId: 'chat-agent-v1',
    sessionId: 'sess_456'
  });

  try {
    await trace.thought(`Processing message: ${userMessage}`);
    
    const intent = await classifyIntent(userMessage);
    await trace.decision('intent', { intent, confidence: 0.88 });
    
    await trace.action('generate_response', { intent });
    const response = await generateResponse(userMessage, intent);
    
    await trace.output(response);
    return response;
    
  } finally {
    await trace.end();
  }
}
```

## Viewing Traces

### Web Dashboard

Visit http://localhost:8080 to:
- Browse recent traces
- Search by agent, time, or metadata
- View trace details
- Monitor agent performance

### API Queries

```bash
# Get recent traces
curl http://localhost:8080/api/v1/traces?limit=10

# Get specific trace
curl http://localhost:8080/api/v1/traces/{trace_id}

# Query by agent
curl http://localhost:8080/api/v1/traces?agent_id=support-agent-v1

# Advanced query
curl -X POST http://localhost:8080/api/v1/traces/query \
  -H "Content-Type: application/json" \
  -d '{
    "filters": {
      "agent_id": "support-agent-v1",
      "timestamp_from": "2024-01-01T00:00:00Z",
      "semantics.intent": "refund"
    },
    "limit": 100
  }'
```

### Using Glyphtrail

For rich visualization:

```bash
# Install Glyphtrail (connects to ActiveMirrorOS)
docker run -d \
  --name glyphtrail \
  -p 3000:3000 \
  -e ACTIVEMIRROR_URL=http://activemirror:8080 \
  mirrordna/glyphtrail:latest
```

Visit http://localhost:3000 for interactive trace exploration.

## Next Steps

1. **Explore the API**: Learn all query capabilities in the API documentation
2. **Configure storage**: Optimize storage for your scale
3. **Set up monitoring**: Configure dashboards and alerts
4. **Deploy to production**: Follow deployment best practices

## Troubleshooting

### Connection refused

```bash
# Check if ActiveMirrorOS is running
docker ps | grep activemirror

# Check logs
docker logs activemirror
```

### Database connection errors

```bash
# Verify database is reachable
docker exec -it activemirror ping db

# Check connection string in config
cat /etc/activemirror/activemirror.yaml
```

### Traces not appearing

```python
# Enable debug logging
client = MirrorDNAClient(
    url="http://localhost:8080",
    debug=True  # Prints trace events
)
```

## Support

- **Documentation**: [Full API docs](https://docs.activemirror.io)
- **GitHub Issues**: [Report bugs](https://github.com/MirrorDNA-Reflection-Protocol/ActiveMirrorOS/issues)
- **Community**: [Discord server](https://discord.gg/mirrordna)

---

*Start building observable AI today!* 🚀
