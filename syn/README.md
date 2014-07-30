# syn

Be sure to include the proper environment variables.

You'll need the following set to something reasonable if you're running the script outside of docker:
```  
  export INTERFACE=SomeInterface
  export TARGET=SomeTarget
  export PORT=SomePort
```

Otherwise you can pass the variables in via docker on start.
### Usage
1. `docker build --rm=true --tag="dtaas/syn" ./`
2. `docker run -d -e INTERFACE=SomeInterface -e TARGET=SomeTarget -e PORT=SomePort dtaas/syn:latest`

### Warning
This can seriously mess up someone's day. It will shoot syn packets as fast as possible at the target. Please use for testing only.
