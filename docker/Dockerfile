# Use a lightweight Python base image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirement.txt .
RUN pip install --no-cache-dir -r requirement.txt

# Copy the necessary folders for inference
COPY scripts/p8-inference.py ./scripts/
COPY models/fraud_detector_v1.pkl ./models/
COPY input-data/raw/balanced_creditcard.csv ./input-data/raw/

# Command to run the detector when the container starts
CMD ["python", "scripts/p8-inference.py"]
