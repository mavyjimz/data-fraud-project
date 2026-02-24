# Data Fraud Project: End-to-End MLOps Pipeline
**Status:** Phase 14 Complete (CI/CD Production Ready)
**Hardware:** ZenBook-UX433FN (NVIDIA MX150) | i5 Linux Node [cite: 2026-02-23]
**Registry:** ghcr.io/mavyjimz/data-fraud-project:latest

## Project Infrastructure
- scripts/: Python logic following pX-phase-name.py pattern [cite: 2026-02-20]
- docker/: Production blueprints including Dockerfile for GHCR
- .github/workflows/: CI/CD automation using Classic PAT (GH_PAT)
- input-data/: Source Kaggle creditcard.csv and processed balanced datasets [cite: 2026-02-23]
- requirements.txt: Environment lockfile (scikit-learn, mlflow, dotenv)

---

## Curriculum and Workflow
- Lesson #1: Initialized MLOps directory structure and Git repository [cite: 2026-01-26]
- Lesson #2: Setup venv-mlops and installed core data science libraries [cite: 2026-02-23]
- Lesson #3: Data Ingestion. Imported and verified raw creditcard.csv [cite: 2026-02-23]
- Lesson #4: Class Imbalance Audit. Identified 492 fraud cases (0.17%) [cite: 2026-02-23]
- Lesson #5: Data Balancing. Applied random under-sampling for 50/50 dataset [cite: 2026-02-23]
- Lesson #6: Model Training. Implemented Logistic Regression (92% Recall) [cite: 2026-02-23]
- Lesson #7: Model Persistence. Exported trained model to .pkl format [cite: 2026-02-23]
- Lesson #8: Model Inference. Successfully performed prediction on random samples [cite: 2026-02-23]
- Lesson #9: Native Linux Containerization. Developed Dockerfile for deployment [cite: 2026-02-23]
- Lesson #10: Production Verification. Verified live inference via REST endpoint [cite: 2026-02-23]
- Lesson #11: Cloud Registry Migration. Integrated GitHub Container Registry (GHCR) [cite: 2026-02-23]
- Lesson #12: Workflow Orchestration. Initialized GitHub Actions for automated triggers
- Lesson #13: Security Vaulting. Implemented Repository Secrets for GH_PAT authentication
- Lesson #14: CI/CD Production. Finalized Docker push and verified GREEN build

---

## Career Achievement Log
- Pipeline Architecture: Designed a modular 14-phase MLOps structure from scratch [cite: 2026-01-25]
- DevOps Integration: Built a secure CI/CD pipeline using GitHub Actions and PAT tokens
- Container Orchestration: Optimized Docker build layers for high-performance ML workloads
- System Hardening: Managed Linux kernel sleep targets and root-level API permissions
