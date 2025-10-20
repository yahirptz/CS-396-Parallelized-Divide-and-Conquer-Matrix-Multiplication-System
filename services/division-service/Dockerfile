FROM python:latest
LABEL Creator="Christian"

COPY services/division-service/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY shared /shared

WORKDIR /
COPY matrix_divide.py ./

EXPOSE 5000:5001

CMD [ "python", "./matrix_divide.py"]