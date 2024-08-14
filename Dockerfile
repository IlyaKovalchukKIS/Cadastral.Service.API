# Используем официальное Python изображение
FROM python:latest

# Устанавливаем рабочую директорию
WORKDIR user/

# Копируем зависимости
COPY src/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD ["alembic", "upgrade", "head"]
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
