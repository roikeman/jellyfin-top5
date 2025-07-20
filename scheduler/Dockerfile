FROM python:3.11-slim

# Install cron
RUN apt-get update && apt-get install -y cron

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY job.py crontab entrypoint.sh ./
RUN chmod 0644 crontab && crontab crontab
RUN chmod +x entrypoint.sh job.py

ENTRYPOINT ["./entrypoint.sh"]