# Data Fraud Project: Master MLOps Blueprint
**Owner:** Vanjunn & Partner [cite: 2026-02-06]
**Environment:** Linux (ZenBook UX433FN) [cite: 2026-02-23]
**Hardware Specs:** i5 8th Gen | 8GB RAM | NVIDIA MX150 2GB [cite: 2026-02-23]

---

## Phase 1-5: Data Engineering & Imbalance Management
* Infrastructure: Initialized Git and venv-mlops to isolate dependencies [cite: 2026-02-23].
* Data Cleaning: Handled UTF-8 and formatting errors in superstore_sales.csv [cite: 2026-01-23].
* The Problem: Identified extreme class imbalance (only 492 fraud cases vs 284k transactions) [cite: 2026-02-23].
* The Solution: Applied Random Under-sampling to create a balanced balanced_data.csv (984 rows) [cite: 2026-02-23].

---

## Phase 6-8: Model Training & Persistence
* Algorithm: Logistic Regression with a focus on Recall (92%) to ensure no fraud goes undetected [cite: 2026-02-23].
* Naming Logic: All scripts follow pX-phase-name.py for MLOps traceability [cite: 2026-02-20].
* Persistence: Serialized the model brains into models/fraud_model.pkl for API usage [cite: 2026-02-20].

---

## Phase 9-14: Production & Cloud Handshake
* Containerization: Built a python:3.9-slim Docker image for production.
* Thermal Monitoring: Kept the MX150 at 50°C during builds and 41°C during idle serving [cite: 2026-02-23].
* Registry Fix: Performed a Master Key fix by enabling all scopes in GitHub PAT to bypass permission_denied.
* CI/CD Completion: Hardened YAML syntax and successfully triggered a green build in GitHub Actions.

---

## Quick-Reference Commands
* Clear File (nano): Alt + \ -> Ctrl + ^ -> Alt + / -> Ctrl + K [cite: 2026-02-23].
* Clean Build: sudo docker build -t data-fraud-project -f docker/Dockerfile . && sudo docker image prune -f [cite: 2026-01-27, 2026-02-23].
* Git Sync: git add . && git commit -m "update" && git push [cite: 2026-01-19, 2026-01-27].
* Docker Login: echo $GH_PAT | docker login ghcr.io -u mavyjimz --password-stdin [cite: 2026-02-23, 2026-02-24].

---

## Career Achievement Summary
1. Pipeline Architecture: Designed a 14-phase modular MLOps structure [cite: 2026-01-25, 2026-02-20].
2. DevOps Orchestration: Fully automated the transition from local Python scripts to global Cloud Registry images [cite: 2026-01-25, 2026-02-23].
3. Thermal Efficiency: Optimized Docker layers for low-spec hardware (MX150/i5) [cite: 2026-01-25, 2026-02-23].
