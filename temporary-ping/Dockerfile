FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
EXPOSE 8767
CMD ["python", "-m", "gunicorn", "-b", "0.0.0.0:8767", "app:app"]
