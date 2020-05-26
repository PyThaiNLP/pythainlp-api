FROM python:alpine3.6
MAINTAINER Wannaphong Phatthiyaphaibun <wannaphong@kkumail.com>
WORKDIR /usr/src/app
EXPOSE 8000

COPY requirements.txt ./
RUN apt-get install python3-dev
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app"]
