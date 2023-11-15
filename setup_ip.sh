#!/bin/bash
ENV_FILE=$1
IP=$(ifconfig | grep "inet " | grep -Fv 127.0.0.1 | awk '{print $2}' | head -n 1)
sed -i -e "s/localhost/$IP/g" $ENV_FILE
