FROM python:3.11-slim

WORKDIR /app
COPY . /app

# Install exact version
RUN pip install --no-cache-dir prefect==3.4.9

EXPOSE 4200
CMD ["python", "prefect_app/start.py"]

