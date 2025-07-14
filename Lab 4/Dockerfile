FROM python:3.11-slim

WORKDIR /application

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

ENV API_KEY=62fbb4a2e0359346047c8f5b96e0fea1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
