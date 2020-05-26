FROM python:3.6-stretch
MAINTAINER Wannaphong Phatthiyaphaibun <wannaphong@kkumail.com>
WORKDIR /usr/src/app
EXPOSE 8000

COPY requirements.txt ./
RUN apt-get install python3-dev
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app"]
