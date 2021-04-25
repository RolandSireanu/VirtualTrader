FROM ubuntu:groovy

WORKDIR /usr/src/app
RUN apt-get update -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

ENTRYPOINT ["rqscheduler", "--host", "redis-server", "--port", "6379"]