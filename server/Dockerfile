# Используем официальное Python изображение
FROM python:3.12

# Устанавливаем рабочую директорию
WORKDIR /app/app

# Копируем зависимости
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код сервера
COPY . .

# Указываем команду для запуска Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
