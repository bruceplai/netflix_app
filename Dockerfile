from python:3.8-slim-buster

WORKDIR /usr/app

COPY server/* ./
COPY db/* ./

RUN pip install -r requirements.txt
RUN python import_data.py
RUN chmod +x run.sh

EXPOSE 9090

CMD ./run.sh
