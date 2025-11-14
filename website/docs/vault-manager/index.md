---
sidebar_position: 1
title: Vault Manager / LingOS Pro
---

# Vault Manager / LingOS Pro

**Vault Manager** is the enterprise-grade secure storage and management system for MirrorDNA traces, providing encryption, access control, and compliance features for LingOS Pro users.

## Overview

Vault Manager extends the MirrorDNA ecosystem with enterprise security:

- **Encrypted Storage**: AES-256 encryption at rest
- **Access Control**: Fine-grained RBAC
- **Compliance**: SOC2, HIPAA, GDPR ready
- **Audit Logs**: Complete access history
- **Data Residency**: Regional storage options
- **Backup & Recovery**: Automated disaster recovery

## Architecture

```
┌────────────────────────────────────┐
│    LingOS Pro Agent                │
└──────────────┬─────────────────────┘
               │ encrypted traces
               ↓
┌────────────────────────────────────┐
│    Vault Manager                   │
│  ┌──────────────────────────────┐  │
│  │  Encryption Layer            │  │
│  │  (AES-256-GCM)              │  │
│  └──────────────────────────────┘  │
│  ┌──────────────────────────────┐  │
│  │  Access Control (RBAC)       │  │
│  └──────────────────────────────┘  │
│  ┌──────────────────────────────┐  │
│  │  Audit Logger                │  │
│  └──────────────────────────────┘  │
└──────────────┬─────────────────────┘
               │
               ↓
┌────────────────────────────────────┐
│  Secure Storage Backends           │
│  • Encrypted Databases             │
│  • Hardware Security Modules (HSM) │
│  • Cloud KMS (AWS, Azure, GCP)     │
└────────────────────────────────────┘
```

## Key Features

### 1. End-to-End Encryption

Every trace is encrypted before storage:

```python
from lingos_pro import Agent, VaultManager

vault = VaultManager(
    region="us-east-1",
    encryption="AES-256-GCM",
    key_provider="aws-kms"  # or azure-kv, gcp-kms, hsm
)

agent = Agent(
    model="gpt-4",
    vault=vault  # All traces automatically encrypted
)

response = agent.chat("Sensitive medical information...")
# Trace encrypted before storage
```

**Encryption Details**:
- Algorithm: AES-256-GCM
- Key rotation: Automatic (configurable)
- Key storage: HSM or cloud KMS
- Zero-knowledge: Vault Manager can't decrypt without keys

### 2. Role-Based Access Control

Fine-grained permissions:

```python
from lingos_pro import AccessControl, Role, Permission

# Define roles
roles = {
    "developer": Role(
        permissions=[
            Permission.READ_TRACES,
            Permission.SEARCH_TRACES
        ],
        scope={"agent_id": "dev-*"}
    ),
    "auditor": Role(
        permissions=[
            Permission.READ_TRACES,
            Permission.EXPORT_TRACES,
            Permission.VIEW_AUDIT_LOGS
        ],
        scope="all"
    ),
    "admin": Role(
        permissions=Permission.ALL,
        scope="all"
    )
}

# Assign roles
vault.access_control.assign_role(
    user="jane@company.com",
    role="auditor"
)
```

### 3. Compliance Profiles

Pre-configured compliance settings:

```python
from lingos_pro import ComplianceProfile

# HIPAA compliance
vault = VaultManager(
    compliance=ComplianceProfile.HIPAA(
        encryption_required=True,
        access_logging=True,
        data_residency="US",
        retention_days=2555,  # 7 years
        phi_auto_redaction=True
    )
)

# GDPR compliance
vault = VaultManager(
    compliance=ComplianceProfile.GDPR(
        encryption_required=True,
        data_residency="EU",
        right_to_deletion=True,
        right_to_export=True,
        consent_tracking=True
    )
)
```

### 4. Audit Logging

Complete access history:

```python
# Query audit logs
logs = vault.audit_logs.query(
    user="jane@company.com",
    action=["READ", "EXPORT"],
    date_from="2024-01-01",
    date_to="2024-01-31"
)

for log in logs:
    print(f"{log.timestamp}: {log.user} {log.action} trace {log.trace_id}")
```

**Audit Log Contents**:
- Who accessed what
- When access occurred
- What action was performed
- IP address and location
- Success/failure status
- Data exported (if any)

### 5. Data Residency

Store data in specific regions:

```python
# EU data stays in EU
vault_eu = VaultManager(
    region="eu-west-1",
    data_residency="EU"
)

# US data stays in US
vault_us = VaultManager(
    region="us-east-1",
    data_residency="US"
)

# Multi-region with residency rules
vault_multi = VaultManager(
    regions=["us-east-1", "eu-west-1", "ap-southeast-1"],
    residency_rules={
        "user.country": {
            "US": "us-east-1",
            "EU": "eu-west-1",
            "APAC": "ap-southeast-1"
        }
    }
)
```

### 6. Backup & Recovery

Automated disaster recovery:

```python
vault = VaultManager(
    backup=BackupPolicy(
        frequency="daily",
        retention_days=90,
        cross_region=True,
        destinations=["s3://backup-bucket", "azure://backup-container"]
    )
)

# Restore from backup
vault.restore(
    backup_id="backup-2024-01-15",
    target_region="us-west-2"
)
```

## LingOS Pro Integration

Vault Manager is tightly integrated with LingOS Pro:

```python
from lingos_pro import Agent, VaultManager, ComplianceProfile

# Create vault-backed agent
vault = VaultManager(
    region="us-east-1",
    compliance=ComplianceProfile.SOC2
)

agent = Agent(
    model="gpt-4",
    vault=vault,
    agent_id="customer-support-pro"
)

# All traces automatically:
# - Encrypted
# - Compliance-checked
# - Access-controlled
# - Audit-logged

response = agent.chat("User query...")
```

## Security Features

### Key Management

```python
vault = VaultManager(
    key_provider="aws-kms",
    key_rotation_days=90,
    key_hierarchy={
        "master_key": "aws-kms://us-east-1/master",
        "data_encryption_keys": "auto-generated",
        "dek_rotation": "per-trace"  # or daily, weekly
    }
)
```

### Zero-Knowledge Architecture

Vault Manager uses client-side encryption:

```python
# Encryption happens in LingOS Pro agent before sending
agent = Agent(
    model="gpt-4",
    vault=VaultManager(encryption="client-side")
)

# Vault Manager never sees plaintext traces
# Only encrypted data stored
```

### Network Security

```python
vault = VaultManager(
    network_security={
        "tls_version": "1.3",
        "allowed_ips": ["10.0.0.0/8"],
        "vpn_required": True,
        "mfa_required": True
    }
)
```

## Compliance Features

### HIPAA

```python
from lingos_pro import HIPAAVault

vault = HIPAAVault(
    encryption="AES-256",
    access_logging=True,
    phi_detection=True,
    breach_notification=True,
    minimum_necessary=True,
    baa_compliant=True
)

# Automatic PHI detection and protection
agent = Agent(model="gpt-4", vault=vault)
response = agent.chat("Patient SSN: 123-45-6789")
# SSN automatically detected and encrypted
```

### GDPR

```python
from lingos_pro import GDPRVault

vault = GDPRVault(
    data_residency="EU",
    consent_required=True,
    right_to_deletion=True,
    right_to_export=True,
    purpose_limitation=True
)

# Handle data subject requests
vault.delete_user_data(user_id="user_123")  # Right to erasure
vault.export_user_data(user_id="user_123")  # Right to portability
```

### SOC 2

```python
from lingos_pro import SOC2Vault

vault = SOC2Vault(
    trust_service_criteria=["security", "availability", "confidentiality"],
    change_management=True,
    incident_response=True,
    monitoring=True
)

# Generate SOC 2 evidence
evidence = vault.generate_soc2_report(
    period="2024-Q1",
    criteria=["security", "confidentiality"]
)
```

## Deployment

### Managed Cloud

Fully managed Vault Manager:

```bash
# Sign up for LingOS Pro
lingos-pro signup

# Create vault
lingos-pro vault create \
  --name production-vault \
  --region us-east-1 \
  --compliance HIPAA,SOC2

# Get vault credentials
lingos-pro vault credentials production-vault
```

### Self-Hosted

Deploy in your infrastructure:

```bash
# Kubernetes deployment
helm install vault-manager mirrordna/vault-manager \
  --set encryption.provider=aws-kms \
  --set compliance.profiles=HIPAA,GDPR \
  --set storage.backend=postgresql

# Docker deployment
docker run -d \
  --name vault-manager \
  -e KMS_PROVIDER=aws \
  -e KMS_KEY_ID=arn:aws:kms:... \
  -e DATABASE_URL=postgresql://... \
  mirrordna/vault-manager:latest
```

### Hybrid

Mix managed and self-hosted:

```python
vault = VaultManager(
    control_plane="managed",  # Managed by LingOS Pro
    data_plane="self-hosted"  # Data stays in your infrastructure
)
```

## Pricing

### LingOS Pro (includes Vault Manager)

| Tier | Storage | Encryption | Compliance | Support | Price |
|------|---------|------------|------------|---------|-------|
| **Starter** | 10 GB | ✅ | Basic | Email | $99/mo |
| **Professional** | 100 GB | ✅ | GDPR, SOC2 | Priority | $499/mo |
| **Enterprise** | Unlimited | ✅ | All + Custom | 24/7 SLA | Custom |

### Add-ons

- Additional storage: $0.10/GB/month
- Cross-region backup: +20%
- HSM key storage: $200/month
- Custom compliance: Custom pricing

## Migration

### From Open Source to Pro

```python
# Step 1: Install LingOS Pro
pip install lingos-pro

# Step 2: Migrate existing traces
from lingos_pro import migrate_to_vault

migrate_to_vault(
    source_activemirror="http://localhost:8080",
    destination_vault=vault,
    encrypt=True,
    verify=True
)

# Step 3: Update agents
agent = Agent(
    model="gpt-4",
    vault=vault  # Now using Vault Manager
)
```

### From ActiveMirrorOS to Vault Manager

```bash
# Export from ActiveMirrorOS
activemirror export --format mirrordna --output traces.jsonl

# Import to Vault Manager
lingos-pro vault import \
  --vault production-vault \
  --file traces.jsonl \
  --encrypt
```

## Monitoring

### Health Dashboard

Monitor vault health:

```python
health = vault.health_check()

print(f"Status: {health.status}")
print(f"Encryption: {health.encryption_status}")
print(f"Storage: {health.storage_used}/{health.storage_capacity}")
print(f"Backup: {health.last_backup}")
```

### Alerts

Configure alerts:

```python
vault.alerts.configure([
    Alert("high_storage_usage", threshold=0.9, action="email"),
    Alert("encryption_key_expiry", days_before=7, action="page"),
    Alert("unauthorized_access_attempt", action="block_and_alert"),
    Alert("compliance_violation", action="immediate_page")
])
```

## Best Practices

1. **Use HSM for production**: Hardware key storage for critical systems
2. **Enable cross-region backups**: Disaster recovery
3. **Rotate keys regularly**: 90-day rotation recommended
4. **Monitor audit logs**: Review access patterns weekly
5. **Test recovery**: Regular disaster recovery drills
6. **Principle of least privilege**: Minimal necessary permissions
7. **Enable MFA**: Multi-factor authentication for all users

## Resources

- **LingOS Pro**: [Get started](https://lingos.ai/pro)
- **Docs**: [Vault Manager guide](https://docs.lingos.ai/pro/vault-manager)
- **Security**: [Security whitepaper](https://lingos.ai/security)
- **Compliance**: [Compliance docs](https://lingos.ai/compliance)
- **Support**: [pro-support@lingos.ai](mailto:pro-support@lingos.ai)

---

*Enterprise security for AI traces.* 🔐
