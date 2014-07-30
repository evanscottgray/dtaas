# pps

Awesomesauce dns pps attack.

Be sure to include the proper environment variables.

You'll need the following set to something reasonable if you're running the script outside of docker:

```shell
export TARGET=SomeTarget
export THREADS=SomeAmountBetween10AndLike30
```

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
1. `docker build --rm=true --tag="dtaas/pps" ./`
2. `docker run -d --privileged=true dtaas/pps:latest`

### Warning

This can kill things on the network.
