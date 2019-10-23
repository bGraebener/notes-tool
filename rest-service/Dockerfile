FROM python:3-alpine

RUN pip install flask flask_pymongo flask_cors

COPY ./app.py .

EXPOSE 5000

ENTRYPOINT [ "flask", "run" ]