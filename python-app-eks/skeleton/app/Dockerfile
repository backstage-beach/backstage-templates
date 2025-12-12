FROM python:${{ values.python_version }}-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

ENV PORT=${{ values.container_port }}

EXPOSE ${{ values.container_port }}

CMD ["gunicorn", "--bind", "0.0.0.0:${{ values.container_port }}", "app:app"]
