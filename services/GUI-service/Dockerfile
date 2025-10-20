FROM python:latest
LABEL Creator="Christian"

WORKDIR /app
COPY services/aggregation-service/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY shared /shared
COPY services/GUI-service/gui.py .

EXPOSE 5000

CMD [ "python", "./gui.py"]