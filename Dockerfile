# Python base image
FROM python:3.10-slim

# System dependencies for OpenCV and Dlib
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    build-essential \
    cmake \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Environment variable for Cloud display (optional)
ENV PYTHONUNBUFFERED=1

CMD ["python", "main.py"]
