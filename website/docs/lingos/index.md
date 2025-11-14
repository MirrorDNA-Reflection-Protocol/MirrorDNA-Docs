---
sidebar_position: 1
title: LingOS
---

# LingOS

**LingOS** is a conversational AI framework built from the ground up with MirrorDNA observability baked in. Create powerful, traceable AI agents with full transparency.

## Overview

LingOS provides:

- **Conversational AI**: Build chat, voice, and multimodal agents
- **Built-in MirrorDNA**: Every conversation automatically traced
- **Two Editions**: Lite (open-source) and Pro (enterprise)
- **Framework Agnostic**: Works with any LLM provider

## LingOS Lite vs Pro

| Feature | Lite (Open Source) | Pro (Enterprise) |
|---------|-------------------|------------------|
| **MirrorDNA Tracing** | ✅ Full support | ✅ Full support |
| **LLM Providers** | OpenAI, Anthropic, open models | + Azure, AWS Bedrock, private models |
| **Deployment** | Self-hosted | Self-hosted + managed cloud |
| **Vault Manager** | ❌ | ✅ Secure trace storage |
| **Compliance** | Basic | TrustByDesign integration |
| **Support** | Community | Enterprise SLA |
| **License** | MIT | Commercial |

## Key Features

### 1. Zero-Config Tracing

```python
from lingos import Agent

# Tracing is automatic!
agent = Agent(
    model="gpt-4",
    activemirror_url="http://localhost:8080"
)

response = agent.chat("Hello!")
# Trace automatically sent to ActiveMirrorOS
```

### 2. Rich Agent Primitives

```python
agent = Agent(model="gpt-4")

# Thought process
agent.think("User wants product recommendations")

# Tool use
results = agent.use_tool("search_products", query="laptops")

# Decision making
if agent.decide("user_is_frustrated", confidence=0.8):
    agent.escalate_to_human()

# Response
agent.respond("Here are some great laptops...")
```

### 3. Multi-Turn Conversations

```python
from lingos import Conversation

conv = Conversation(agent_id="sales-bot")

# Turn 1
conv.user("I'm looking for a laptop")
conv.agent("What's your budget?")

# Turn 2
conv.user("Around $1000")
conv.agent("Here are some options...")

# All turns tracked in single trace
```

### 4. RAG (Retrieval-Augmented Generation)

```python
from lingos import RAGAgent

agent = RAGAgent(
    model="gpt-4",
    knowledge_base="product_docs",
    embedding_model="text-embedding-ada-002"
)

# Automatically retrieves and cites sources
response = agent.chat("How do I reset my password?")
# Response includes citations, all tracked in MirrorDNA
```

### 5. Tool Integration

```python
from lingos import tools

@tools.define
def get_weather(location: str) -> dict:
    """Get current weather for a location"""
    # Your implementation
    return {"temp": 72, "condition": "sunny"}

agent = Agent(model="gpt-4", tools=[get_weather])

response = agent.chat("What's the weather in SF?")
# Tool calls automatically traced
```

## Architecture

```
┌─────────────────────────────────────┐
│     LingOS Agent Application        │
└──────────────┬──────────────────────┘
               │
    ┌──────────┴──────────┐
    │                     │
    ↓                     ↓
┌─────────┐        ┌──────────────┐
│   LLM   │        │ ActiveMirror │
│Provider │        │     OS       │
└─────────┘        └──────────────┘
                          ↓
                   ┌──────────────┐
                   │  MirrorDNA   │
                   │   Traces     │
                   └──────────────┘
```

## Quick Start

### LingOS Lite (Open Source)

```bash
# Install
pip install lingos

# Create agent
from lingos import Agent

agent = Agent(
    model="gpt-4",
    api_key="your-openai-key",
    activemirror_url="http://localhost:8080"
)

# Chat
response = agent.chat("Tell me about MirrorDNA")
print(response)
```

### LingOS Pro

```bash
# Install Pro edition
pip install lingos-pro

# Authenticate
lingos login

# Create managed agent
from lingos_pro import Agent, VaultManager

vault = VaultManager(region="us-east-1")

agent = Agent(
    model="gpt-4",
    vault=vault,  # Secure trace storage
    compliance=["GDPR", "HIPAA"]
)

response = agent.chat("Sensitive query...")
# Traces encrypted and stored in Vault
```

## Use Cases

### Customer Support

```python
from lingos import Agent, Knowledge

kb = Knowledge.from_docs("./support_docs")

support_agent = Agent(
    model="gpt-4",
    name="Support Agent",
    knowledge=kb,
    personality="helpful and patient"
)

# Handle customer queries with full traceability
```

### Sales Assistant

```python
from lingos import Agent, CRM

crm = CRM.connect("salesforce")

sales_agent = Agent(
    model="gpt-4",
    tools=[crm.get_lead, crm.update_opportunity],
    goal="qualify and convert leads"
)
```

### Code Assistant

```python
from lingos import CodeAgent

code_agent = CodeAgent(
    model="gpt-4",
    languages=["python", "javascript"],
    can_execute=True,  # Safely run code
    trace_execution=True
)

result = code_agent.solve("Write a function to reverse a string")
```

## Advanced Features (Pro)

### Compliance Profiles

```python
from lingos_pro import Agent, ComplianceProfile

# GDPR-compliant agent
gdpr_agent = Agent(
    model="gpt-4",
    compliance=ComplianceProfile.GDPR(
        auto_redact_pii=True,
        right_to_deletion=True,
        data_residency="EU"
    )
)
```

### Multi-Agent Orchestration

```python
from lingos_pro import AgentTeam

team = AgentTeam([
    Agent(name="Researcher", role="gather information"),
    Agent(name="Analyst", role="analyze data"),
    Agent(name="Writer", role="compose response")
])

# Agents collaborate, traces linked
result = team.solve("Write a market analysis report")
```

### Human-in-the-Loop

```python
from lingos_pro import Agent, HumanReview

agent = Agent(
    model="gpt-4",
    review=HumanReview(
        require_approval_for=["refunds", "sensitive_data"],
        escalate_on_low_confidence=0.7
    )
)

# Pauses for human approval when needed
```

## Integration with Ecosystem

- **ActiveMirrorOS**: Automatic trace storage
- **Glyphtrail**: Visualize conversation flows
- **TrustByDesign**: Compliance checking
- **AgentDNA**: Load personality profiles
- **Vault Manager**: Secure Pro features

## Deployment

### Docker

```bash
docker run -d \
  --name lingos-agent \
  -e OPENAI_API_KEY=your-key \
  -e ACTIVEMIRROR_URL=http://activemirror:8080 \
  mirrordna/lingos:latest
```

### Kubernetes

```bash
helm install lingos mirrordna/lingos \
  --set llm.provider=openai \
  --set llm.apiKey=your-key
```

### Serverless

```python
# AWS Lambda handler
from lingos import Agent

agent = Agent(model="gpt-4")

def lambda_handler(event, context):
    response = agent.chat(event["message"])
    return {"response": response}
```

## Comparison with Other Frameworks

| Framework | MirrorDNA | Multi-Modal | RAG | Tools | Observability |
|-----------|-----------|-------------|-----|-------|---------------|
| **LingOS** | ✅ Native | ✅ | ✅ | ✅ | ✅ Built-in |
| LangChain | ⚠️ Plugin | ✅ | ✅ | ✅ | ⚠️ Via callbacks |
| AutoGPT | ⚠️ Plugin | ❌ | ⚠️ | ✅ | ❌ Limited |
| Semantic Kernel | ❌ | ⚠️ | ✅ | ✅ | ⚠️ Basic |

## Roadmap

Coming soon:

- **Voice agents**: Built-in speech-to-text/text-to-speech
- **Multimodal**: Vision, image generation
- **Memory**: Long-term agent memory with MirrorDNA
- **Marketplace**: Pre-built agent templates

## Resources

- **GitHub**: [LingOS](https://github.com/MirrorDNA-Reflection-Protocol/LingOS)
- **Docs**: [Full API reference](https://docs.lingos.ai)
- **Examples**: [Sample agents](https://github.com/MirrorDNA-Reflection-Protocol/LingOS/tree/main/examples)
- **Pro**: [Get started with Pro](https://lingos.ai/pro)

---

*Conversational AI with full transparency.* 💬
