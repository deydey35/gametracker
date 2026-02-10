FROM python:3.11-slim

# Installation du client MySQL pour les scripts bash 
RUN apt-get update && apt-get install -y default-mysql-client bash && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt 

COPY . .

RUN chmod +x scripts/*.sh

CMD ["./scripts/run_pipeline.sh"] 