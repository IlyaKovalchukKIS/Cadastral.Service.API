# Используем официальное Python изображение
FROM python:3.12

# Устанавливаем рабочую директорию
WORKDIR user/src

# Копируем зависимости
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код сервера
COPY . ./src
COPY .env .
COPY alembic.ini .
# Указываем команду для запуска Uvicorn

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
