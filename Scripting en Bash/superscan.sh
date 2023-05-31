#!/bin/bash
#
# Ejemplo de Menu en BASH
#
date
    echo "|"
    echo "|---------------------------|"
    echo "|   Menu Principal          |"
    echo "|---------------------------|"
    echo "|1. Net Discover"
    echo "|2. PortScan"
    echo "|3. Welcome"
    echo "|4. Exit"
    echo "|"
read -p "Opción  [ 1 - 4 ] " c
case $c in
        1) source netdiscover.sh;;
        2) read -p "Escribe la direccion ip: " ipp; source portscanv1.sh $ipp ;;
        3) source welcome.sh;;
        4) echo "Bye!"; exit 0;;
esac