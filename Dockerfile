FROM python:slim-buster

LABEL maintainer="Python Barranquilla <info@pybaq.co>"

WORKDIR /app

RUN apt-get update && \
    apt-get install -y python-dev libssl-dev libffi-dev imagemagick && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

# Production requirements
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Testing requirements
# COPY ./test-requirements.txt /app/test-requirements.txt
# RUN pip install -r test-requirements.txt

COPY . /app/

ENTRYPOINT [ "lektor" ]
CMD ["server", "-h", "0.0.0.0"]
