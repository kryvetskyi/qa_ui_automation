#! /bin/bash 

set -e

sudo docker run -d \
	-p 4444:4444 \
	--shm-size="2g" \
	--restart always \
	selenium/standalone-chrome:4.10.0-20230607
