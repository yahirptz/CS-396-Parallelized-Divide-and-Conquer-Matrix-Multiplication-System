FROM python:latest
LABEL Creator="Christian"

COPY services/multiplication-service/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /
COPY matrix_multiply.py ./

EXPOSE 5000:5002

CMD [ "python", "./matrix_multiply.py"]