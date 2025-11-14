---
sidebar_position: 2
title: Semantic Annotations
---

# Semantic Annotations

MirrorDNA's **semantic layer** adds rich meaning and context to traces, transforming raw event logs into intelligent, queryable knowledge.

## What are Semantic Annotations?

Semantic annotations are structured metadata that describe:

- **Intent**: What the agent is trying to accomplish
- **Context**: Situational information
- **Quality**: Confidence, relevance, importance
- **Compliance**: Privacy, security, regulatory markers
- **Relationships**: Links between events and entities

## Annotation Types

### Intent Classification

Classify the purpose of agent actions:

```json
{
  "event_id": "evt_123",
  "type": "thought",
  "content": "User wants to book a flight",
  "semantics": {
    "intent": "flight_booking",
    "intent_category": "transaction",
    "confidence": 0.95
  }
}
```

**Standard Intent Taxonomy**:
- `information_seeking`
- `transaction`
- `troubleshooting`
- `social`
- `creative`

### Confidence Scores

Track certainty at each decision point:

```json
{
  "event_id": "evt_456",
  "type": "decision",
  "content": "Classifying user sentiment as positive",
  "semantics": {
    "confidence": 0.87,
    "alternatives": [
      {"label": "neutral", "confidence": 0.11},
      {"label": "negative", "confidence": 0.02}
    ]
  }
}
```

### Privacy Markers

Annotate sensitive data handling:

```json
{
  "event_id": "evt_789",
  "type": "observation",
  "content": "[REDACTED]",
  "semantics": {
    "privacy": {
      "contains_pii": true,
      "pii_types": ["email", "phone"],
      "redaction_method": "hash",
      "gdpr_relevant": true
    }
  }
}
```

### Citations and Sources

Track information provenance:

```json
{
  "event_id": "evt_101",
  "type": "output",
  "content": "The capital of France is Paris",
  "semantics": {
    "citations": [
      {
        "source": "knowledge_base",
        "document_id": "geography_europe",
        "confidence": 1.0
      }
    ]
  }
}
```

### Error Attribution

When things go wrong, track why:

```json
{
  "event_id": "evt_error",
  "type": "error",
  "content": "Failed to retrieve user profile",
  "semantics": {
    "error_category": "external_service",
    "error_code": "SERVICE_TIMEOUT",
    "severity": "medium",
    "recoverable": true,
    "recovery_action": "retry_with_backoff"
  }
}
```

## Custom Semantics

Extend the standard with domain-specific annotations:

```json
{
  "event_id": "evt_medical",
  "type": "decision",
  "content": "Recommending diagnostic test",
  "semantics": {
    "medical": {
      "icd10_code": "R50.9",
      "urgency": "routine",
      "specialty": "internal_medicine"
    }
  }
}
```

## Semantic Queries

Use annotations to power intelligent search:

```javascript
// Find all high-confidence transactions
traces.query({
  "semantics.intent_category": "transaction",
  "semantics.confidence": { $gt: 0.9 }
})

// Find privacy incidents
traces.query({
  "semantics.privacy.contains_pii": true,
  "semantics.privacy.gdpr_relevant": true
})

// Find errors by category
traces.query({
  "type": "error",
  "semantics.error_category": "external_service"
})
```

## Benefits

### 1. Intelligent Debugging

Quickly find events by intent, not just text matching:
- "Show me all failed payment transactions"
- "Find low-confidence medical diagnoses"

### 2. Compliance Automation

Automatically flag traces requiring review:
- GDPR-relevant PII handling
- High-risk decisions
- Regulatory-sensitive domains

### 3. Quality Monitoring

Track agent performance over time:
- Average confidence scores
- Error rates by category
- Intent coverage

### 4. Behavioral Analysis

Understand patterns:
- Which intents lead to errors?
- How does confidence correlate with user satisfaction?
- What citation sources are most reliable?

## Best Practices

### 1. Be Consistent

Use the standard taxonomy when possible; only create custom annotations when necessary.

### 2. Add Context

Include enough semantic information to understand events in isolation.

### 3. Track Uncertainty

Always include confidence scores for probabilistic decisions.

### 4. Mark Privacy

Err on the side of caution—mark potential PII liberally.

### 5. Link Events

Use semantic relationships to connect related events:

```json
{
  "event_id": "evt_final",
  "type": "output",
  "semantics": {
    "derived_from": ["evt_001", "evt_003", "evt_007"],
    "reasoning_chain": "inference"
  }
}
```

## Semantic Schema

The full semantic schema is defined in the [MirrorDNA Specification](https://github.com/MirrorDNA-Reflection-Protocol/MirrorDNA-Standard/blob/main/spec/semantics.md).

Key schema elements:

- `intent`: String (from standard taxonomy or custom)
- `confidence`: Float [0.0, 1.0]
- `privacy`: Object (PII markers, GDPR flags)
- `citations`: Array of source references
- `error_category`: String (for error events)
- `custom`: Object (domain-specific extensions)

## Future Directions

Upcoming semantic features:

- **Causal graphs**: Explicit cause-effect relationships
- **Counterfactuals**: "What if" annotations
- **Multi-modal**: Semantic tags for images, audio
- **Ontology linking**: Connect to external knowledge graphs

---

*Making AI traces intelligently searchable.* 🔍
