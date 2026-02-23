# Data Fraud Project: End-to-End MLOps Pipeline
**Status:** Phase 11 Complete | **Hardware:** ZenBook-UX433FN (NVIDIA MX150) [cite: 2026-02-23]

## Project Infrastructure
- scripts/: Python logic following pX-phase-name.py pattern [cite: 2026-02-20]
- input-data/: Source Kaggle creditcard.csv and processed balanced datasets
- output-data/: Generated artifacts and logs [cite: 2026-02-23]
- models/: Storage for serialized (.pkl) model brains [cite: 2026-02-20]
- requirement.txt: Environment lockfile (scikit-learn, pandas, numpy) [cite: 2026-02-23]

---

## Curriculum and Workflow
- Lesson #1: Initialized MLOps directory structure and Git repository [cite: 2026-01-26, 2026-02-23]
- Lesson #2: Setup venv-mlops and installed core data science libraries [cite: 2026-02-23]
- Lesson #3: Data Ingestion. Imported and verified raw creditcard.csv from Kaggle
- Lesson #4: Class Imbalance Audit. Identified 492 fraud cases (0.17%) in 284k transactions [cite: 2026-02-23]
- Lesson #5: Data Balancing. Applied random under-sampling to create a 50/50 balanced dataset [cite: 2026-02-23]
- Lesson #6: Model Training. Implemented Logistic Regression with 92% Recall performance [cite: 2026-02-23]
- Lesson #7: Model Persistence. Exported trained model to pkl format [cite: 2026-02-23]
- Lesson #8: Model Inference. Successfully performed prediction on random samples [cite: 2026-02-23]
- Lesson #9: Native Linux Containerization. Developed Dockerfile for API deployment [cite: 2026-02-23]
- Lesson #10: Production Verification. Verified live inference via browser-based REST endpoint [cite: 2026-02-23]
- Lesson #11: Cloud Registry Migration. Integrated GitHub Container Registry (GHCR) [cite: 2026-02-23]

---

## Career Achievement Log
- Pipeline Architecture: Designed a modular 10-phase MLOps structure from scratch [cite: 2026-01-25, 2026-02-20]
- Data Engineering: Successfully handled extreme class imbalance using resampling techniques [cite: 2026-01-25, 2026-02-23]
- Environment Management: Utilized pip freeze and .nanorc for reproducible dev environments [cite: 2026-01-25, 2026-02-23]
