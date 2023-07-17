FROM python:3.11-slim-bullseye

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y allure

CMD ["pytest", "--alluredir=reports/allure-results", "tests/test_alerts.py"]
