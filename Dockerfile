FROM python:3.11-slim-bullseye

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["pytest", "--alluredir=reports/allure-results", "tests/test_alerts.py"]
