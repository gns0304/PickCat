FROM python:3.8
ENV PYTHONUNBUFFERED=1
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN apt-get update \
    && apt-get install -y \
        libsqlclient-dev libssl-dev \
    && rm -rf /var/lib/apt/lists/*
RUN pip install -r requirements.txt
RUN chmod +x /app/run.sh
EXPOSE 8000

ENTRYPOINT ["/app/run.sh"]