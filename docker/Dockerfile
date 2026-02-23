# Use a lightweight Python base image for our Linux environment [cite: 2026-02-23]
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Install dependencies in one layer to maximize build efficiency [cite: 2026-02-23]
RUN pip install --no-cache-dir pandas scikit-learn joblib fastapi uvicorn

# Copy our Independent R&D assets into the container [cite: 2026-02-23]
COPY models/ /app/models/
COPY input-data/raw/balanced_creditcard.csv /app/input-data/raw/
COPY scripts/p9-api-interface.py /app/scripts/

# Expose port 8000 for our FastAPI service [cite: 2026-02-23]
EXPOSE 8000

# Launch the API server when the container starts [cite: 2026-02-23]
CMD ["uvicorn", "scripts.p9-api-interface:app", "--host", "0.0.0.0", "--port", "8000"]
