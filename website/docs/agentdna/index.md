---
sidebar_position: 1
title: AgentDNA
---

# AgentDNA

**AgentDNA** is a persona engine that defines consistent, reliable AI agent personalities and behaviors, encoded in MirrorDNA format for full observability.

## What is AgentDNA?

AgentDNA lets you:

- **Define** agent personalities with structured profiles
- **Version** agent behaviors for reproducibility
- **Test** personas against scenarios
- **Deploy** consistent agents across platforms
- **Observe** how personas influence decisions

Think of it as "character sheets" for AI agents, but with the rigor of software configuration.

## Core Concepts

### Agent Persona

A **persona** defines:

```yaml
# agent_persona.yaml
name: "Customer Support Specialist"
version: "2.1.0"

personality:
  traits:
    - empathetic
    - patient
    - solution-oriented
  tone: "professional yet warm"
  formality: medium
  
capabilities:
  - answer_product_questions
  - troubleshoot_issues
  - process_refunds
  - escalate_to_human

constraints:
  - never_make_promises
  - never_share_internal_info
  - always_verify_identity
  
knowledge_domains:
  - product_catalog
  - return_policy
  - shipping_procedures

response_style:
  max_length: 200
  use_emoji: false
  cite_sources: true
  ask_clarifying_questions: true

mirrordna:
  trace_all_decisions: true
  semantic_tags:
    - customer_service
    - support_tier_1
```

### Behavioral Templates

Pre-defined patterns:

```python
from agentdna import BehavioralTemplate

# Professional assistant
professional = BehavioralTemplate.Professional(
    formality="high",
    brevity="concise",
    personality="helpful"
)

# Creative collaborator  
creative = BehavioralTemplate.Creative(
    imagination="high",
    risk_tolerance="medium",
    personality="enthusiastic"
)

# Analytical expert
analytical = BehavioralTemplate.Analytical(
    rigor="high",
    citation_required=True,
    personality="objective"
)
```

### Persona Library

Pre-built personas for common use cases:

- **Customer Support**: Empathetic, solution-focused
- **Sales Assistant**: Persuasive, relationship-building
- **Technical Support**: Detail-oriented, methodical
- **Teacher**: Patient, encouraging, adaptive
- **Researcher**: Thorough, skeptical, citation-focused
- **Creative Writer**: Imaginative, stylistic, flexible

## How It Works

```
┌─────────────────────┐
│  AgentDNA Profile   │
│  (YAML/JSON)        │
└──────────┬──────────┘
           │
           ↓
┌─────────────────────┐
│  Persona Compiler   │
│  - Validates        │
│  - Optimizes        │
│  - Generates prompts│
└──────────┬──────────┘
           │
           ↓
┌─────────────────────┐
│  LingOS Agent       │
│  + Persona          │
└──────────┬──────────┘
           │
           ↓
┌─────────────────────┐
│  MirrorDNA Traces   │
│  (with persona tags)│
└─────────────────────┘
```

## Creating a Persona

### Method 1: YAML Configuration

```yaml
# sales_assistant.yaml
name: "Sales Development Rep"
version: "1.0.0"

personality:
  traits:
    - persuasive
    - friendly
    - goal-oriented
  communication_style: "conversational"
  energy_level: "high"

goals:
  primary: "qualify and convert leads"
  secondary:
    - "build rapport"
    - "identify pain points"
    - "schedule demos"

tools:
  - crm_lookup
  - send_email
  - schedule_meeting

behavioral_rules:
  - rule: "Always ask about budget early"
    priority: high
  - rule: "Mirror prospect's communication style"
    priority: medium
  - rule: "Never discount without manager approval"
    priority: critical

success_metrics:
  - name: "meeting_scheduled"
    weight: 1.0
  - name: "positive_sentiment"
    weight: 0.5
```

### Method 2: Python API

```python
from agentdna import Persona, Trait, Goal

persona = Persona(
    name="Research Assistant",
    traits=[
        Trait.THOROUGH,
        Trait.SKEPTICAL,
        Trait.CITATION_FOCUSED
    ],
    goals=[
        Goal("Find accurate information"),
        Goal("Cite all sources"),
        Goal("Flag uncertainty")
    ],
    constraints=[
        "Never speculate beyond data",
        "Always provide confidence scores",
        "Cite primary sources when possible"
    ]
)

persona.save("research_assistant.yaml")
```

### Method 3: Interactive Builder

```bash
agentdna create --interactive

? Agent name: Marketing Copywriter
? Primary role: Create engaging marketing content
? Personality (select): 
  ✓ creative
  ✓ persuasive
  ✓ brand-aware
? Tone: casual
? Formality: low
? Tools available: 
  ✓ brand_guidelines_lookup
  ✓ competitor_analysis
  ✓ A/B testing

✅ Persona created: marketing_copywriter.yaml
```

## Using Personas

### With LingOS

```python
from lingos import Agent
from agentdna import load_persona

# Load persona
persona = load_persona("customer_support.yaml")

# Create agent with persona
agent = Agent(
    model="gpt-4",
    persona=persona
)

# Agent behavior matches persona
response = agent.chat("I want a refund!")
# Response will be empathetic, follow refund procedures
```

### Multi-Persona Agents

```python
from agentdna import PersonaSwitch

# Define context-dependent personas
persona_switch = PersonaSwitch({
    "technical_query": load_persona("technical_support.yaml"),
    "billing_query": load_persona("billing_specialist.yaml"),
    "general": load_persona("general_support.yaml")
})

agent = Agent(
    model="gpt-4",
    persona_switch=persona_switch
)

# Agent switches personas based on query type
```

### Persona Testing

```python
from agentdna import PersonaTester

tester = PersonaTester(persona="sales_assistant.yaml")

# Test scenarios
results = tester.run_scenarios([
    {
        "input": "I'm not interested",
        "expected_behavior": "acknowledge, ask open question",
        "expected_sentiment": "respectful"
    },
    {
        "input": "What's the price?",
        "expected_behavior": "qualify before pricing",
        "expected_sentiment": "helpful"
    }
])

print(f"Persona consistency: {results.consistency_score}")
print(f"Failed scenarios: {results.failures}")
```

## Persona Versioning

Track persona evolution:

```bash
# Version 1.0.0 - Initial
agentdna create sales_assistant.yaml

# Version 1.1.0 - Added email tool
agentdna update sales_assistant.yaml --add-tool send_email

# Version 2.0.0 - Major personality shift
agentdna update sales_assistant.yaml --personality consultative

# Compare versions
agentdna diff sales_assistant@1.0.0 sales_assistant@2.0.0

# Rollback if needed
agentdna rollback sales_assistant --to-version 1.1.0
```

## MirrorDNA Integration

Every persona decision is traced:

```json
{
  "event_id": "evt_001",
  "type": "decision",
  "content": "Choosing empathetic response pattern",
  "semantics": {
    "persona": {
      "name": "Customer Support Specialist",
      "version": "2.1.0",
      "trait_activated": "empathetic",
      "behavioral_rule": "acknowledge_frustration_first"
    }
  }
}
```

Analyze persona effectiveness:

```python
from agentdna import PersonaAnalytics

analytics = PersonaAnalytics(persona="sales_assistant")

# How does this persona perform?
metrics = analytics.compute_metrics(
    traces=last_30_days,
    success_criteria=["meeting_scheduled", "positive_sentiment"]
)

print(f"Success rate: {metrics.success_rate}")
print(f"Avg confidence: {metrics.avg_confidence}")
print(f"Common failure modes: {metrics.failure_patterns}")
```

## Persona Marketplace

Browse and share personas:

```bash
# Search marketplace
agentdna search "customer service"

# Install public persona
agentdna install zendesk/tier1-support

# Publish your persona
agentdna publish my-sales-assistant --public
```

**Popular Personas**:
- `openai/friendly-assistant` - General purpose helper
- `anthropic/thoughtful-tutor` - Educational support
- `huggingface/code-reviewer` - Technical code review
- `mirrordna/compliant-healthcare` - HIPAA-aware medical

## Best Practices

### 1. Start with Templates

Don't create from scratch—customize existing templates.

### 2. Test Thoroughly

Run scenario tests before production deployment.

### 3. Version Carefully

Use semantic versioning: major.minor.patch

### 4. Monitor Performance

Track persona effectiveness through MirrorDNA analytics.

### 5. Iterate Based on Data

Use traces to identify where personas succeed/fail.

## Persona Composition

Combine multiple personas:

```python
from agentdna import compose_personas

# Create hybrid persona
hybrid = compose_personas(
    base="customer_support.yaml",
    mixins=[
        ("technical_expert.yaml", weight=0.3),
        ("sales_assistant.yaml", weight=0.2)
    ]
)

# Results in support agent with technical depth and sales awareness
```

## Advanced Features

### Emotional Intelligence

```yaml
emotional_intelligence:
  detect_user_emotion: true
  adapt_tone_to_emotion: true
  empathy_level: high
  emotional_responses:
    frustrated: "acknowledge and de-escalate"
    excited: "match energy"
    confused: "simplify and clarify"
```

### Cultural Awareness

```yaml
cultural_adaptation:
  regions: ["US", "EU", "APAC"]
  language_formality:
    US: "casual"
    EU: "formal"
    APAC: "respectful"
  avoid_idioms: true
  date_time_formats: localized
```

### Learning from Feedback

```python
from agentdna import PersonaLearner

learner = PersonaLearner(persona="support_agent")

# Agent learns from user feedback
learner.learn_from_traces(
    traces_with_positive_feedback,
    traces_with_negative_feedback
)

# Suggests persona improvements
suggestions = learner.suggest_improvements()
# "Consider increasing empathy_level for frustrated users"
```

## Use Cases

1. **Consistent Brand Voice**: Ensure all AI agents match brand personality
2. **Specialized Experts**: Deploy domain-specific expert personas
3. **A/B Testing**: Compare persona effectiveness
4. **Compliance**: Encode regulatory constraints in personas
5. **Training**: Onboard new team members with reference personas

## Resources

- **GitHub**: [AgentDNA](https://github.com/MirrorDNA-Reflection-Protocol/AgentDNA)
- **Persona Library**: [Public personas](https://personas.agentdna.io)
- **Examples**: [Sample persona configurations](https://github.com/MirrorDNA-Reflection-Protocol/AgentDNA/tree/main/personas)
- **Docs**: [Full specification](https://docs.agentdna.io)

---

*Personality for AI agents.* 🎭
