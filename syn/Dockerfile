# dtaas/syn
#
# VERSION               0.0.1

FROM python:2
MAINTAINER Evan Gray <evan@evanscottgray.com>

RUN 	apt-get update && apt-get upgrade -y && apt-get install -y git
ADD 	./pyflood.py /

ENTRYPOINT 	python /pyflood.py
