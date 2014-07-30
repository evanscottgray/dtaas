# dtaas/pps
#
# VERSION               0.0.1

FROM python:2
MAINTAINER Evan Gray <evan@evanscottgray.com>

RUN 	apt-get update && apt-get upgrade -y && apt-get install -y wget git unzip tcpdump
RUN   wget http://www.secdev.org/projects/scapy/files/scapy-latest.zip && unzip scapy-latest.zip && cd scapy-2.* && python setup.py install
ADD 	./pps.py /

ENTRYPOINT 	python /pps.py
