# Lightweight Python image
FROM python:3.10-slim

#S# Set working directory inside container
WORKDIR /app

# Copy dependency file first (Docker cache optimization)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Create logs directory (will be mounted as volume)
RUN mkdir -p logs

# Run robot service
CMD ["python", "main.py"]