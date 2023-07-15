FROM python:3.11-slim-bullseye

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 4444

CMD ["pytest", "tests/test_alerts.py"]


