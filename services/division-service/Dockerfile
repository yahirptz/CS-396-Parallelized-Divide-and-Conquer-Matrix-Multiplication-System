FROM python:latest
LABEL Creator="Christian"

COPY services/division-service/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY shared /shared

WORKDIR /
COPY services/division-service/matrix_divide.py ./

EXPOSE 5001

CMD [ "python", "-u", "./matrix_divide.py"]