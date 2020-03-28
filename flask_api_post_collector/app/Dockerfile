FROM python:3.7.6-alpine

ENV GROUP_ID=1000 \
    USER_ID=1000

WORKDIR /var/www/

COPY requirements.txt /var/www/
RUN pip install -r requirements.txt

RUN addgroup -g $GROUP_ID www
RUN adduser -D -G $USER_ID -G www www -s /bin/sh

USER www
COPY app.py /var/www

EXPOSE 5000

CMD [ "python", "app.py"]
