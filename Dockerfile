FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /url_shortener

WORKDIR /url_shortener

ADD . /url_shortener/
#COPY requirements.txt /connekt/
RUN pip install -r requirements.txt

#RUN python manage.py collectstatic --noinput
#COPY . /code/
CMD ["python", "manage.py", "runserver", "0.0.0.0", "8000"]

#ENTRYPOINT ["python", "manage.py"]
#CMD ["runserver", "0.0.0.0:8000"]