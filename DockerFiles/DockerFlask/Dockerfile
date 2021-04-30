FROM python:3.9
ENV PYTHONBUFFERED 1
ENV REDIS_HOST redis-server
ENV DATABASE_HOST db
ENV POSTGRES_PASSWORD 1234
ENV POSTGRES_DB trader
WORKDIR /application
COPY ./requirements.txt /application/requirements.txt

RUN pip3 install -r /application/requirements.txt 

COPY ./application /application 
COPY ./startApp.py /startApp.py
COPY ./entrypoint.sh /entrypoint.sh 

RUN chmod +x /entrypoint.sh

EXPOSE 5000

WORKDIR /

ENTRYPOINT /entrypoint.sh

# CMD python3 /startApp.py
