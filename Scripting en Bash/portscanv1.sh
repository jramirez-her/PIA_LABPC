#!/bin/bash
#Script netdiscover.sh
#07/03/2023-Joaquin Ramirez Hernandez
direccion_ip=$1
puertos="20,21,22,23,25,50,51,53,80,110,119,135,136,137,138,139,143,161,162,389,443,445,636, 1025,1443,3389,5985,5986,8080,10000"
[ $# -eq 0 ] && { echo "Modo de uso: $0 <direccion ip>"; exit 1; }


IFS=,
for port in $puertos
do
    timeout 1 bash -c "echo > /dev/tcp/$direccion_ip/$port > /dev/null 2>&1" &&\
    echo $direccion_ip":"$port" is open"\
    ||\
    echo $direccion_ip":"$port" is closed"
done