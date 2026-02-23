# 🛡️ Data Fraud Project: End-to-End MLOps Pipeline
**Status:** Phase 11 Complete | **Hardware:** ZenBook-UX433FN (NVIDIA MX150) [cite: 2026-02-23]

## 🛠 Project Infrastructure
- `scripts/`: Python logic following `pX-phase-name.py` pattern. [cite: 2026-02-20]
- `input-data/`: Source CSV files (Raw and Balanced). [cite: 2026-01-10, 2026-02-23]
- `output-data/`: Generated artifacts and logs. [cite: 2026-02-23]
- `models/`: Storage for serialized (.pkl) model brains. [cite: 2026-02-20]
- `requirement.txt`: Environment lockfile (scikit-learn, pandas, numpy). [cite: 2026-02-23]

---

## 📚 Curriculum & Workflow
- **Lesson #1**: Initialized MLOps directory structure and Git repository. [cite: 2026-01-26, 2026-02-23]
- **Lesson #2**: Setup `venv-mlops` and installed core data science libraries. [cite: 2026-02-23]
- **Lesson #3**: Data Ingestion. Handled `superstore_sales.csv` errors and moved to credit card data. [cite: 2026-01-23, 2026-02-04]
- **Lesson #4**: Class Imbalance Audit. Identified only 492 fraud cases (0.17%) in 284k transactions. [cite: 2026-02-23]
- **Lesson #5**: Data Balancing. Applied random under-sampling to create a 50/50 balanced dataset (984 rows). [cite: 2026-02-23]
- **Lesson #6**: Model Training. Implemented Logistic Regression with 92% Recall performance. [cite: 2026-02-23]
- **Lesson #7**: Model Persistence Complete. Model reached optima within 1000 iterations. [cite: 2026-02-23]
- **Lesson #8**: Model Inference Complete. Successfully loaded .pkl artifact and performed prediction on random sample [cite: 2026-02-23]
- **Lesson #9**: Native Linux Containerization. [cite: 2026-02-23]
- **Lesson #10**: Production Verification. Verified live inference via browser-based REST endpoint (/predict). [cite: 2026-02-23]
- **Lesson #11**: Cloud Registry Migration. Successfully integrated GitHub Container Registry (GHCR) into the pipeline. [cite: 2026-02-23]

---

## 🚀 Career Achievement Log
- **Pipeline Architecture**: Designed a modular 10-phase MLOps structure from scratch. [cite: 2026-01-25, 2026-02-20]
- **Data Engineering**: Successfully handled extreme class imbalance using resampling techniques. [cite: 2026-01-25, 2026-02-23]
- **Environment Management**: Utilized `pip freeze` and `.nanorc` for reproducible dev environments. [cite: 2026-01-25, 2026-02-23]
