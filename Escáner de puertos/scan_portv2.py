#Script scan_portv2.py
#24/04/2023-Joaquin Ramirez Hernandez
#Parte 1
#Importamos librerias
import socket
#
# Parte 2
def scan(addr, port):
    #Creando un nuevo socket
    socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Estableciendo el timeout para el nuevo objeto tipo socket
    socket.setdefaulttimeout(1)

    #Conecion exitosa devuelve 0. Devuelve error en caso contrario
    result = socket_obj.connect_ex((addr, port)) #Direccion y puerto en tupla

    #Se cierra el objeto
    socket_obj.close()
    
    return result
#
# Parte 3
#Se establece una lista de puertos a escanear
ports=[21,22,25,80]
#
# Parte 4
#bucle por todas las ip del rango 192.168.100.*

for i in range(1, 255):
    addr="192.168.100.{}".format(i)
    for port in ports:
        result= scan(addr, port)
        if result==0:
            print(addr, port, "OK")
        else:
            print(addr, port, "Failed")