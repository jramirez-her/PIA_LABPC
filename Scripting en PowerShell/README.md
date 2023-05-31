# PIA_LABPC
# Producto integrador de aprendizaje de la materia Laboratorio de programación para ciberseguridad

## Scripting en Power Shell 
**Objetivo:** Mostrar ejemplos de scripts en PowerShell
Esta sección se trató algunos ejemplos de scripts desarrollados en PowerShell con tal de ver que tan útil es esta herramienta.
Entre los scripts:
- [scan_alivev1.ps1](https://github.com/jramirez-her/PIA_LABPC/blob/main/Scripting%20en%20PowerShell/scan_alivev1.ps1)
* [scan_alivev2.ps1](https://github.com/jramirez-her/PIA_LABPC/blob/main/Scripting%20en%20PowerShell/scan_alivev2.ps1)
+ [scan_portv1.ps1](https://github.com/jramirez-her/PIA_LABPC/blob/main/Scripting%20en%20PowerShell/scan_portv1.ps1)

### scan_alivev1.ps1
Script que mediante algunas funciones de PowerShell extrae el Gateway de tu red y mediante éste el rango de tu subred. Y mediante una lista previamente establecida con los valores del 1 al 254 representando a los hosts en esta subred. Con la información extraída podemos hacer pings a los 254 hosts que podría haber en la red para ver cuales IPs están activas y cuáles no.

### scan_alivev2.ps1
Script que usa su antecesor *scan_alivev1.ps1* y le da un poco de formato a la salida agregando un título indicando que información es la que sale. De igual manera determina mediante funciones de PowerShell el Gateway de la subred, el rango de la subred y con esto también determina la máscara de red. Los imprime en pantalla y mediante pings verifica que IPs responden según la máscara extraída.

### scan_portv1.ps1
Este script toma como base el *scan_alivev2.ps1* como base para tomar algunas de sus funciones como extraer el Gateway y mediante este determinar el rango de tu subred. Extrae también tu dirección IP, así con una lista de puertos con servicios más comunes previamente establecida en el código, hacemos una conexión al puerto para ver si está abierto o no, si responde la respuesta será afirmativa e imprimirá los resultados.


