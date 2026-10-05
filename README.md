# AI Platform Engineering Journey

> A hands-on learning and homelab project documenting my progression from Infrastructure Operations Engineering towards DevOps, Platform Engineering and AI Platform Engineering.

This repository combines structured learning, practical exercises, infrastructure automation and a working homelab environment.

The goal is not simply to deploy technologies, but to understand how they work and demonstrate that knowledge through documented learning and practical projects.

---

## About Me

I currently work as an **Infrastructure Operations Engineer (Compliance)** supporting enterprise infrastructure, including restricted and air-gapped environments.

My existing experience includes:

- Windows Server Administration
- Microsoft SCCM / MECM
- WSUS
- VMware vSphere / ESXi
- Proxmox VE
- Tenable.sc Vulnerability Management
- Server Compliance & Patch Management
- Enterprise Infrastructure Support
- Infrastructure Troubleshooting
- PowerShell Automation
- Networking Fundamentals

I am currently developing the skills required to move towards:

- DevOps Engineering
- Platform Engineering
- AI Platform Engineering

My main areas of development are:

- Python
- Linux
- Git & GitHub
- Docker
- Kubernetes
- Terraform
- Ansible
- CI/CD
- Cloud Platforms
- AI Infrastructure
- GPU-based AI workloads

---

# Current Focus

## Python Fundamentals

I am currently working through the **Boot.dev DevOps Engineer learning path**, starting with Python fundamentals.

Rather than copying course solutions into this repository, I use Boot.dev as the structured learning platform and document:

- Concepts I have learned
- Notes written in my own words
- Original Python exercises
- Infrastructure-focused examples
- Practical applications to my homelab

Current course:

**Boot.dev → Learn Python for Beginners**

| Chapter | Status |
|---|---|
| 01 - Introduction | ✅ Complete |
| 02 - Variables | ✅ Complete |
| 03 - Functions | ✅ Complete |
| 04 - Scope | ⬜ Not Started |
| 05 - Testing & Debugging | ⬜ Not Started |
| 06 - Computing | ⬜ Not Started |
| 07 - Comparisons | ⬜ Not Started |
| 08 - Loops | ⬜ Not Started |
| 09 - Lists | ⬜ Not Started |
| 10 - Dictionaries | ⬜ Not Started |
| 11 - Sets | ⬜ Not Started |
| 12 - Errors | ⬜ Not Started |
| 13 - Type Hints | ⬜ Not Started |
| 14 - Practice | ⬜ Not Started |
| 15 - Quiz | ⬜ Not Started |

Boot.dev learning work can be found under:

`python/bootdev/`

My original infrastructure-focused Python exercises are available under:

`python/labs/`

---

# Learning Philosophy

This repository separates **having technology running** from **understanding and deliberately learning that technology**.

For example, I already operate a Kubernetes environment in my homelab, but Kubernetes will remain an active learning area until I have worked through the fundamentals and demonstrated that knowledge through this repository.

For each major topic I aim to:

1. Learn the core concepts.
2. Document them in my own words.
3. Complete original exercises.
4. Apply the concepts to infrastructure-related scenarios.
5. Use the technology in my homelab.
6. Automate or improve the environment where appropriate.
7. Commit meaningful progress to GitHub.

---

# Learning Roadmap

## Git & GitHub

- [x] Core Git Fundamentals
- [ ] Branching
- [ ] Merge Conflicts
- [ ] Pull Requests
- [ ] GitHub Actions
- [ ] CI/CD Workflows

---

## Python

### Fundamentals

Currently being completed through Boot.dev.

- [x] Variables & Data Types
- [x] Functions
- [ ] Scope
- [ ] Comparisons
- [ ] Conditionals
- [ ] Loops
- [ ] Lists
- [ ] Dictionaries
- [ ] Sets
- [ ] Error Handling
- [ ] Type Hints
- [ ] Testing & Debugging

### Python for Infrastructure

- [ ] File Handling
- [ ] JSON
- [ ] HTTP Requests
- [ ] REST APIs
- [ ] Virtual Environments
- [ ] Python Packaging
- [ ] Logging
- [ ] Environment Variables
- [ ] API Authentication

### Python for Platform Engineering

- [ ] FastAPI
- [ ] Proxmox API
- [ ] Docker SDK
- [ ] Kubernetes Python Client
- [ ] Infrastructure Automation
- [ ] Monitoring / Health Check Tools

### Python for AI Infrastructure

- [ ] AI Model APIs
- [ ] OpenAI-compatible APIs
- [ ] Local Model APIs
- [ ] Model Serving Automation
- [ ] GPU Workload Automation
- [ ] AI Platform Tooling

---

## Linux

- [ ] Linux Fundamentals
- [ ] Filesystem & Permissions
- [ ] Users & Groups
- [ ] Processes
- [ ] Networking
- [ ] Services / systemd
- [ ] Package Management
- [ ] Logging
- [ ] Bash / Shell Scripting
- [ ] Linux Troubleshooting

---

## Docker & Containers

- [ ] Container Fundamentals
- [ ] Images
- [ ] Dockerfiles
- [ ] Volumes
- [ ] Networking
- [ ] Docker Compose
- [ ] Container Security
- [ ] Container Troubleshooting

---

## Kubernetes

### Fundamentals

- [ ] Kubernetes Architecture
- [ ] Control Plane
- [ ] Worker Nodes
- [ ] Pods
- [ ] Deployments
- [ ] ReplicaSets
- [ ] Services
- [ ] Namespaces
- [ ] ConfigMaps
- [ ] Secrets
- [ ] Storage
- [ ] Ingress
- [ ] Resource Requests & Limits
- [ ] Health Probes

### Platform Engineering

- [ ] Helm
- [ ] RBAC
- [ ] Network Policies
- [ ] Observability
- [ ] Persistent Storage
- [ ] GPU Workloads
- [ ] Application Deployment
- [ ] Kubernetes Troubleshooting
- [ ] Upgrade Strategy
- [ ] High Availability Concepts

---

## Terraform

- [ ] HCL Fundamentals
- [ ] Providers
- [ ] Resources
- [ ] Variables
- [ ] Outputs
- [ ] State
- [ ] Modules
- [ ] Proxmox Provider
- [ ] VM Provisioning
- [ ] Infrastructure Automation

---

## Ansible

- [ ] YAML Fundamentals
- [ ] Inventory
- [ ] Playbooks
- [ ] Variables
- [ ] Templates
- [ ] Roles
- [ ] Idempotency
- [ ] Linux Configuration
- [ ] Kubernetes Node Configuration

---

## CI/CD

- [ ] GitHub Actions
- [ ] Automated Testing
- [ ] Linting
- [ ] Build Pipelines
- [ ] Container Builds
- [ ] Security Scanning
- [ ] Deployment Pipelines
- [ ] GitOps Concepts

---

## Cloud

Future learning will include at least one major cloud platform.

Potential focus:

- Azure
- AWS

Topics will include:

- Compute
- Networking
- Identity
- Storage
- Infrastructure as Code
- Kubernetes
- Monitoring
- Security

---

# Homelab Platform

Alongside the structured learning path, I operate a homelab used to apply these technologies in a real environment.

## Proxmox

The lab currently runs on Proxmox VE and provides the virtual infrastructure for the platform.

Proxmox will eventually be managed increasingly through:

- Terraform
- Ansible
- Python
- Infrastructure-as-Code workflows

---

## Kubernetes / K3s

A working K3s cluster is already deployed.

Current topology:

```text
K3s Cluster

Control Plane
└── k3s-control

Workers
├── k3s-worker-1
└── k3s-worker-2
