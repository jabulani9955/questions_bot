FROM python:3.10

WORKDIR /app
COPY req.txt req.txt
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r req.txt

RUN chmod 755 .

COPY init_docker_postgres.sh /docker-entrypoint-initdb.d/

COPY . .