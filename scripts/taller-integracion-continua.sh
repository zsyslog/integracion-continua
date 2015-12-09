#!/bin/bash

cd /var/www/taller-integracion-continua

if [ "$1" -eq "1" ]; then
    git pull
fi
if [ "$1" -eq "0" ]; then
    docker stop taller-integracion-continua_$3
    docker rm taller-integracion-continua_$3
    docker pull $2
    docker run -v /var/www/taller-integracion-continua:/var/www -d -i -t --name taller-integracion-continua_$3 $2 /bin/bash
    git pull origin $3
fi
