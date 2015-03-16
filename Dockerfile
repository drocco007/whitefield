FROM python:3-slim
MAINTAINER Daniel Rocco <drocco@gmail.com>

EXPOSE 6543

ADD . /home/whitefield

WORKDIR /home/whitefield

RUN ["python", "setup.py", "develop"]

CMD ["python","-m","whitefield.mobile"]
