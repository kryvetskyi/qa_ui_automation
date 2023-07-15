FROM python:3.11-slim-bullseye

WORKDIR /app

# Установка инструмента ожидания wait-for-it.sh
RUN apt-get update && apt-get install -y wget && \
    wget https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh -O /usr/local/bin/wait-for-it.sh && \
    chmod +x /usr/local/bin/wait-for-it.sh && \
    apt-get remove -y wget && \
    rm -rf /var/lib/apt/lists/*

# Копирование всех файлов в контейнер
COPY . .

# Установка зависимостей Python
RUN pip install -r requirements.txt

# Добавление прав выполнения для docker-entrypoint.sh
RUN chmod +x docker-entrypoint.sh

EXPOSE 4444

CMD ["./docker-entrypoint.sh"]

