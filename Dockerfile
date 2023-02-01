FROM python:3.10

WORKDIR /app
COPY req.txt req.txt
RUN pip3 install --upgrade setuptools
RUN pip3 install -r req.txt

RUN chmod 755 .

COPY . .