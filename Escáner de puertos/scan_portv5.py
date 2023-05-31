#Script scan_portv5.py
#24/04/2023-Joaquin Ramirez Hernandez
import nmap


op1='y'
escaner= nmap.PortScanner()

while(op1!='n'):
    print("======================Bienvenido======================\n: ")
    print("=============================================")
    print("QUE DESEA REALIZAR")
    print("(1) Escaneo UDP\n(2) Escaneo completo\n(3) Detección de sistema operativo\n(4) Escaneo de red con ping")
    print("=============================================")
    op2=int(input())
    if(op2==1):
        print("Ingresa la IP a realizar el escaneo UDP: ")
        ip=input()
        print("Ingresa el rango de puertos a escanear(de esta forma: 1-1024)")
        ports=input()
        print("..........ESCANEANDO..........")
        print(escaner.scan(ip, ports, '-sU'))
        print("Puertos encontrados: {}".format((escaner[ip]['udp'].keys())))
    elif(op2==2):
        print("Ingresa la IP a realizar el escaneo COMPLETO: ")
        ip=input()
        print("Ingresa el rango de puertos a escanear(de esta forma: 1-1024)")
        ports=input()
        print("..........ESCANEANDO..........")
        print(escaner.scan(ip, ports, '-v -A'))
    elif(op2==3):
        print("Ingresa la IP a realizar el escaneo con deteccion de SO: ")
        ip=input()
        ports='1-30000'
        print(escaner.scan(ip, None, '-O'))
        print("SISTEMA OPERATIVO: {}".format(escaner[ip]['osmatch'][1]['name']))
    elif(op2==4):
        print("Ingresa el nombre de la red a escanear por ping (Ejem---> 192.168.100.0/24 )")
        ip=input()
        ports='1-30000'
        print(escaner.scan(ip, None, '-sn'))
        print("IP encontradas activas dentro de la red: {}".format(escaner.all_hosts()))
    print("¿Desea realizar algo mas?[Y/N]")
    op1=input().lower()
    