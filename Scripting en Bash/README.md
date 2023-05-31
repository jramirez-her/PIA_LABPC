# PIA_LABPC
# Producto integrador de aprendizaje de la materia Laboratorio de programación para ciberseguridad
## Scripting en Bash
**Objetivo:** Mostrar ejemplos de scripts en Bash
Esta sección se trató algunos ejemplos de scripts desarrollados en Bash con tal de ver que tan útil es esta herramienta.
Entre los scripts:
- [bro.sh](https://github.com/jramirez-her/PIA_LABPC/blob/main/Scripting%20en%20Bash/bro.sh)
* [netdiscover.sh](https://github.com/jramirez-her/PIA_LABPC/blob/main/Scripting%20en%20Bash/netdiscover.sh)
+ [number.sh](https://github.com/jramirez-her/PIA_LABPC/blob/main/Scripting%20en%20Bash/number.sh)
- [portscanv1.sh](https://github.com/jramirez-her/PIA_LABPC/blob/main/Scripting%20en%20Bash/portscanv1.sh)
* [superscan.sh](https://github.com/jramirez-her/PIA_LABPC/blob/main/Scripting%20en%20Bash/superscan.sh)
+ [welcome.sh](https://github.com/jramirez-her/PIA_LABPC/blob/main/Scripting%20en%20Bash/welcome.sh)

### welcome.sh
Este script imprime en consola una bienvenida al usuario que incluye:
- El nombre del usuario
* La fecha
+ Usuarios conectados y sus procesos.

### bro.sh
Script que lee un nombre que ingresa el usuario y mediante este imprime un saludo concatenando el nombre y un saludo previamente establecido.

### netdiscover.sh
Script que descubre hosts activos en nuestra red. Mediante comando básicos como ifconfig para saber nuestra IP extrae la dirección y de la misma manera también la subred. Luego hace pings a los posibles 254 hosts que pueda haber en la subred. Si el ping es exitoso indicará que el host está activo e imprime el resultado en consola.

### portscanv1.sh
Este script de igual forma que el anterior extrae la dirección IP del usuario y mediante una lista de puertos previamente establecida accede al directorio /dev/tcp/ y mediante la IP y un ciclo itera los puertos para comprobar si se puede acceder al directorio, de ser asi el puerto estará abierto. Imprime los resultados en consola según sea el caso.


### superscan.sh
Este script es un menú con varias herramientas las cuales son los scripts que anteriormente realizamos:
1. Netdiscover: Ejecutará el script *netdiscover.sh*
2. Portscanv1: Ejecutará el script *portscanv1.sh*
3. Welcome: Ejecutará el script *welcome.sh*
4. Exit: Detendrá la ejecución del programa
Cada opción realiza lo mismo que ya se describió con anterioridad.
