# PIA_LABPC
# Producto integrador de aprendizaje de la materia Laboratorio de programación para ciberseguridad
## Envío de correos
**Objetivo:** Mostrar el envío de correos con Python
Esta sección se desarrolló un ejemplo de cómo enviar correos mediante Python.

Entre los scripts:
- [enviocorreo.py](https://github.com/jramirez-her/PIA_LABPC/blob/main/Env%C3%ADo%20de%20correos/enviocorreo.py)



### enviocorreo.py
Con la librería **EmailMessage** podemos darle formato a nuestro correo, mediante esta librería creamos un objeto y a este objeto le asignamos los parámetros necesarios para el correo como: el cuerpo, asunto, remitente, destinatario.
Asignamos los parámetros correspondientes y mediante la librería **mimetypes** extraemos los bytes de una imagen y los copiamos dentro del cuerpo del correo para adjuntar la imagen y reproducirla dentro.
Mediante el uso de librerías como **smtplib** podemos hacer una conexión por el puerto 587 con *Gmail* para poder realizar el envío de correos. Con el método **SMTP()** en la librería smtplib realizamos una conexión con este puerto para realizar envíos de correos. Después de realizar este proceso iniciamos una sesión TLS (Transport Layer Security) y con el método **login(correo, contraseña)** en la variable que guardamos la conexión del método **SMTP()**, en este método asignamos nuestro correo y contraseña de la app (en este caso de Gmail). Una vez exitoso el *login* usamos el método **sendmail(remitente, destinatario, cuerpo)** el cual recibirá los parámetros correspondientes los cuales hemos definido antes, el cuerpo estará determinado por el que hemos construido con el objeto de la librería **EmailMessage**
