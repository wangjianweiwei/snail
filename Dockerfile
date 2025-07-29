FROM python:3.10.15-slim

WORKDIR /snail
COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["/snail/entrypoint.sh"]