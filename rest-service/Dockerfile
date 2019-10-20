FROM python:3-alpine

RUN pip install flask flask_pymongo

COPY ./app.py .

EXPOSE 5000

ENTRYPOINT [ "flask", "run", "--host", "0.0.0.0" ]