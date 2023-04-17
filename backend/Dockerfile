FROM python:3.11

WORKDIR /code

COPY requirements.txt requirements.txt
RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . .

CMD python3 manage.py makemigrations && \
    python3 manage.py migrate && \
    gunicorn letmecode.wsgi:application --bind 0.0.0.0:8000 --workers 3
