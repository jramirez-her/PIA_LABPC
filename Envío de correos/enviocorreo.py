#Script enviocorreo.py
#02/05/2023-Joaquin Ramirez Hernandez
#Importacion de librerias necesarias
from email.message import EmailMessage
import smtplib
import mimetypes

#Declaracion de variables del remitente, destinatario y contenido del mensaje
remitente = ejemplo@gmail.com
destinatario = alumnol@uanl.edu.mx
mensaje = "<h2><b>Practica 12</b></p></h2> <div>Ejercicio de la practica 12 para envío de correos</div> <div><b>Alumno:</b> Joaquin Ramirez Hernandez</div> <div><b>Matricula:</b> 1860939</div>"

#Mediante el modulo Email damos formato al mensaje
cuerpo = EmailMessage()
cuerpo["From"] = remitente
cuerpo["To"] = destinatario
cuerpo["Subject"] = "Prueba de envio (script Python) - 1860939"
cuerpo.set_content(mensaje, subtype='html')

#Adjunto de la imagen
#Obtenemos el main y sub type de la imagen en este caso es image/png
mime_type= mimetypes.guess_type("../fcfm_cool.png")
#Leemos el contenido de la imagen
with open("../fcfm_cool.png", "rb") as img:
    data = img.read()
    #Se adjunta la imagen al correo con algunas especificaciones
    cuerpo.add_attachment(data, maintype= mime_type[0].split("/")[0], subtype= mime_type[0].split("/")[1], filename="fcfm_cool.jpeg")


#Conexion
#Abrimos una conexion en el puerto 587 para envio de correos
conn= smtplib.SMTP('smtp.gmail.com', 587)
conn.ehlo()
conn.starttls()
conn.login(ejemplo@gmail.com, <contraseña>)
#Se envia el correo ya formado anteriormente
conn.sendmail(remitente , destinatario, cuerpo.as_string())
conn.quit()