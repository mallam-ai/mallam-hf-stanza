FROM python:3.11

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

ADD . .

ENV STANZA_RESOURCES_DIR /code/stanza_resources

RUN python download.py

CMD ["gunicorn", "-k", "sync", "-w", "1", "-b", "0.0.0.0:7860", "main:app"]
