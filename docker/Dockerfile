FROM python:3.9-slim

WORKDIR /app

# The '.' context in YAML means the robot looks in the root
# even though the Dockerfile is in the /docker folder.
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

CMD ["python", "scripts/p1-data-ingestion.py"]
