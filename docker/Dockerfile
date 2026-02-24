FROM python:3.9-slim

WORKDIR /app

# Install dependencies first for faster builds
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy everything else from the root
COPY . .

# Explicitly target the Phase 1 script
CMD ["python", "scripts/p1-data-ingestion.py"]
