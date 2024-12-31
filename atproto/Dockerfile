FROM python:3.13.1-bullseye

RUN mkdir -p /opt/service

WORKDIR /opt/service

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY bin bin

CMD ["/opt/service/bin/run.py"]
