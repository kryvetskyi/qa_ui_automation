#! /bin/bash 

set -e

#docker run --rm -it  -p 4444:4444 -p 5900:5900 -p 7900:7900 --shm-size 2g seleniarm/standalone-chromium:latest

docker run -d \
	-p 4444:4444 \
	--shm-size="2g" \
	--restart always \
	selenium/standalone-chrome
