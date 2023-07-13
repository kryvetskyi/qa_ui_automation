FROM python:3.9-slim-bullseye

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["pytest", "tests/test_form.py"]


