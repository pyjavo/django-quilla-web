FROM python:slim-buster

LABEL maintainer="Python Barranquilla <info@pybaq.co>"

ARG LEKTOR_VERSION="3.1.3"

RUN apt-get update && \
    apt-get install -y python-dev libssl-dev libffi-dev imagemagick && \
    rm -rf /var/lib/apt/lists/*

RUN pip install "Lektor==$LEKTOR_VERSION"

COPY . /app/

WORKDIR /app

ENTRYPOINT [ "lektor" ]
CMD ["server", "-h", "0.0.0.0"]
