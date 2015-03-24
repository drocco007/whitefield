FROM python:3-slim
MAINTAINER Daniel Rocco <drocco@gmail.com>


#
# new security keys
#

# Add the PostgreSQL PGP key to verify their Debian packages.
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8
# Add PostgreSQL's repository. It contains the most recent stable release
#     of PostgreSQL, ``9.4``.
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main" > /etc/apt/sources.list.d/pgdg.list

# ditto for nginx
RUN apt-key adv --keyserver pgp.mit.edu --recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62
RUN echo "deb http://nginx.org/packages/mainline/debian/ wheezy nginx" >> /etc/apt/sources.list

# Update the Ubuntu and PostgreSQL repository indexes
RUN apt-get update


#
# postgres
#

# Install ``python-software-properties``, ``software-properties-common`` and PostgreSQL 9.4
#  There are some warnings (in red) that show up during the build. You can hide
#  them by prefixing each apt-get statement with DEBIAN_FRONTEND=noninteractive
RUN apt-get -y -q install python-software-properties \
    software-properties-common supervisor postgresql-9.4 \
    postgresql-client-9.4 postgresql-contrib-9.4 python3-psycopg2

# Grrrr. Fix psycopg2 install
RUN ln -s  /usr/lib/python3/dist-packages/psycopg2/_psycopg*.so /usr/lib/python3/dist-packages/psycopg2/_psycopg.so
RUN ln -s /usr/lib/python3/dist-packages/psycopg2 /usr/local/lib/python3.4/site-packages/



# Add en_US.UTF-8 locale
RUN locale-gen en_US.UTF-8

# Run the rest of the commands as the ``postgres`` user created by the ``postgres-9.4`` package when it was ``apt-get installed``
USER postgres

# Fix the default encoding (http://jacobian.org/writing/pg-encoding-ubuntu/)
RUN pg_dropcluster --stop 9.4 main &&\
    pg_createcluster --start -e UTF-8 9.4 main

# Create a PostgreSQL role named ``whitefield`` with ``whitefield`` as the password and
# then create a database `whitefield` owned by the ``whitefield`` role.
RUN    /etc/init.d/postgresql start &&\
    psql --command "CREATE USER whitefield PASSWORD 'whitefield';" &&\
    createdb -O whitefield whitefield

# Adjust PostgreSQL configuration so that remote connections to the
# database are possible.
# FIXME: tighten this
RUN echo "host all  all    0.0.0.0/0  trust" >> /etc/postgresql/9.4/main/pg_hba.conf

# And add ``listen_addresses`` to ``/etc/postgresql/9.4/main/postgresql.conf``
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.4/main/postgresql.conf

# Expose the PostgreSQL port
EXPOSE 5432

# Add VOLUMEs to allow backup of config, logs and databases
VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]


#
# nginx
#

USER root

ENV NGINX_VERSION 1.7.10-1~wheezy

RUN apt-get install -y ca-certificates nginx=${NGINX_VERSION} && \
    rm -rf /var/lib/apt/lists/*

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log
RUN ln -sf /dev/stderr /var/log/nginx/error.log

VOLUME ["/var/cache/nginx"]

EXPOSE 80 443


#
# supervisor
#

USER root
RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Set the default command to run when starting the container
CMD ["/usr/bin/supervisord"]


#
# python stuff
#

RUN ["pip", "install", "--use-wheel", "pyramid", "parsedatetime", "waitress"]
