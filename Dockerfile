FROM python:latest

MAINTAINER Larry Shumlich lshumlich@gmail.com

COPY . /web

WORKDIR /web/api

RUN pip install -r ./requirements.txt

# CMD ["gunicorn", "app:app", "--access-logfile -"]

# gunicorn app:app --access-logfile -
# CMD ["gunicorn", "app:app"]
# CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8000"]
# CMD ["gunicorn", "app:app", "-b", "0.0.0.0:$PORT"]
CMD gunicorn app:app --bind 0.0.0.0:$PORT