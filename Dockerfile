FROM python:alpine3.6
MAINTAINER Wannaphong Phatthiyaphaibun <wannaphong@kkumail.com>
WORKDIR /usr/src/app
EXPOSE 8000

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]