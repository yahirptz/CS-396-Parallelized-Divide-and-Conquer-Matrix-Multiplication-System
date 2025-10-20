FROM python:latest
LABEL Creator="Christian"

WORKDIR /app

COPY services/aggregation-service/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY shared /shared
COPY services/aggregation-service/matrix_combine.py .

EXPOSE 5003

CMD [ "python", "./matrix_combine.py"]