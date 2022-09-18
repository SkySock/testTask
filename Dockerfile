FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y gcc python3-dev musl-dev netcat


COPY ./req.txt .
RUN pip install --upgrade pip
RUN pip install -r req.txt

COPY . .

ENTRYPOINT ["./entrypoint.sh"]
