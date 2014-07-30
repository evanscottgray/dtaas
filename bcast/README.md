# bcast

Fire and forget broadcast storm.

### Requirements

This needs Scapy to run, if you're on a Debian based system, this command will install it for you:  

```shell
wget http://www.secdev.org/projects/scapy/files/scapy-latest.zip
unzip scapy-latest.zip
cd scapy-2.*
sudo python setup.py install
```

If not on Debian, just use some google fu.

### Usage
1. `docker build --rm=true --tag="dtaas/bcast" ./`
2. `docker run -d --privileged=true dtaas/bcast:latest`

### Warning
This WILL break things on your network. If you turn it off things will start to work again.
