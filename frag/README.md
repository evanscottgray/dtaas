# frag

Be sure to include the proper environment variables.

You'll need the following set to something reasonable if you're running the script outside of docker:
```  
  export TARGET=SomeTarget
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

Otherwise you can pass the variables in via docker on start.
### Usage
1. `docker build --rm=true --tag="dtaas/frag" ./`
2. `docker run -d --privileged=true -e TARGET=SomeTarget dtaas/frag:latest`

### Warning
This sends invalid tcp fragments. Can freak webservers out and make them cry.
