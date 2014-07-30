# arp

Be sure to include the proper environment variables.

You'll need the following set to something reasonable if you're running the script outside of docker:
```shell  
  export GATEWAY=SomeGateway
  export TARGET=SomeTarget
```

Otherwise you can pass the variables in via docker on start.

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
1. `docker build --rm=true --tag="dtaas/arp" ./`
2. `docker run -d -e TARGET=SomeTarget -e GATEWAY=SomeGateway dtaas/arp:latest`

### Warning
This WILL break things on your network if you're not careful. It will pwn the cam tables on your switches/routers/whatever.
