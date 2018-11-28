FROM python:3.6

LABEL container_name flaskapp
EXPOSE 5000
ADD . /code

RUN apt-get update && apt-get install -y supervisor

COPY nginx.conf /etc/nginx/
COPY uwsgi.ini /etc/uwsgi/
COPY supervisord.conf /etc/

WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "p2app.py"]
#CMD ["/usr/bin/supervisord"]
