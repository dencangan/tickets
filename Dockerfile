FROM python:3.7

WORKDIR /tickets

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "mainApp.py"]