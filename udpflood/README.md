# udpflood

Be sure to include the proper environment variables.

You'll need the following set to something reasonable if you're running the script outside of docker:
```shell  
  export TARGET=SomeTarget
  export THREADS=SomeAmountBetween10AndLike30
  export PACKETSIZE=DefaultsTo1024
```
Otherwise you can pass the variables in via docker on start.

### Usage
1. `docker build --rm=true --tag="dtaas/udpflood" ./`
2. `docker run -d --privileged=true -e TARGET=SomeTarget -e THREADS=SomeAmountBetween10AndLike30 -e PACKETSIZE=DefaultsTo1024 dtaas/udpflood:latest`

### Warning
This CAN break your access to the host you're ssh'd into if you don't have more than 1 interface to access on.
