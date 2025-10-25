FROM python:latest
LABEL Creator="Christian"

COPY services/multiplication-service/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY shared /shared

WORKDIR /
COPY services/multiplication-service/matrix_multiply.py ./

EXPOSE 5002

CMD [ "python", "-u", "./matrix_multiply.py"]