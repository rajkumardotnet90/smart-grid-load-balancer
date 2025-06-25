
FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install flask prometheus_client
CMD ["python", "app.py"]
