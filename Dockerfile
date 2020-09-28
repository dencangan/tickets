FROM python:3.7

WORKDIR /tickets-docker

COPY requirements.txt .

COPY src/ .

RUN pip install -r requirements.txt

CMD ["python", "mainApp.py"]