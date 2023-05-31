# PIA_LABPC
# Producto integrador de aprendizaje de la materia Laboratorio de programación para ciberseguridad
## Escáner de puertos
**Objetivo:** Mostrar un Escáner de puertos en Python
Esta sección se trató algunos ejemplos de scripts desarrollados en Python con la finalidad de hacer escáneres de puertos.

Entre los scripts:
- [scan_portv1.py]()
* [scan_portv2.py]()
+ [scan_portv3.py]()
- [scan_portv5.py]()


### scan_portv1.py
Este script pide como argumentos una dirección IP y un rango de puertos a escanear que se ingresan en la línea de comandos y se obtienen mediante la librería **sys**. Obtenemos el primer puerto y el ultimo y mediante la librería **socket** creamos un objeto *socket* para probar conexión con un puerto en específico. Luego mediante un for iterado por el rango de puertos verificamos mediante el método **.connect_ex(())** en el cual mandamos una tupla con la dirección IP y el puerto a hacer la conexión, si responde un 0 el puerto estará abierto y será almacenado en una lista. Luego se da salida a los puertos abiertos en consola.

### scan_portv2.py
Este script crea una función de nombre *scan(addr, port)* la cual recibe una dirección y un puerto y de igual manera que **scan_portv1.py** mediante la librería **socket** crea un objeto *socket* para mediante el método **.connect_ex(())** haga una conexión y verifique si el puerto está abierto, esta función devuelve el resultado del método **.connect_ex(())**. Mediante una lista de puertos previamente definida con los puertos más comunes iteramos en un ciclo for con un rango de 254 que simulará posibles hosts en la subred. Dentro de este for se agregará un segmento de una red el cual iremos iterando con los números para chequear posibles puertos abiertos en los hosts que respondan dentro de la red. Si el resultado de la función **scan()** es 0 el resultado será exitoso y el puerto estará abierto en el host correspondiente a la iteración.

### scan_portv3.py
Este script funciona de la misma manera que *scan_portv1.py* pero ahora usaremos la librería **threading** para crear hilos y hacer el escaneo más eficiente. Definimos una función *tcp_test(port)* la cual se encargará de verificar mediante la librería **socket** si los puertos están abiertos o no. Después verificamos si el archivo que esta ejecutándose es el main, de serlo así el archivo se ejecutará desde la línea de comandos y ahi mismo se le agregarán los parámetros de la IP a realizar el escaneo y el rango de puertos. Mediante un for iremos iterando mediante el rango de puertos donde por cada puerto iremos agregando un hilo que realice la función y verifique si está abierto el puerto. El resultado podrá notarse mucho más rápido que el otro script y se imprimirá en consola.

### scan_portv4.py
Mediante el uso de la herramienta **NMAP** y la librería **nmap** en Python podemos hacer uso de la misma y realizar escaneos de una forma más sencilla. Este script contiene un menú que realiza las siguientes funciones:
1. Escaneo UDP: Realiza un escaneo por el protocolo UDP para ver que puertos están abiertos en una ip especifica.
2. Escaneo completo: Realiza un escaneo completo sobre una dirección IP
3. Detección de sistema operativo: Detecta el sistema operativo en una dirección IP
4. Escaneo de red con ping: Descubre hosts activos mediante pings
