FROM pg_base
MAINTAINER Daniel Rocco <drocco@gmail.com>


#
# app section
#

EXPOSE 6543

ADD . /home/whitefield

WORKDIR /home/whitefield

RUN ["pip", "install", "--use-wheel", "pyramid_debugtoolbar"]
RUN ["python", "setup.py", "develop"]

COPY docker/whitefield_base/supervisord.conf /etc/supervisor/conf.d/whitefield.conf
COPY docker/whitefield_base/nginx.conf /etc/nginx/conf.d/default.conf
