# PIA_LABPC
# Producto integrador de aprendizaje de la materia Laboratorio de programación para ciberseguridad
## Webscrapping
**Objetivo:** Mostrar ejemplos de scripts que trabajan la extracción de información mediante Webscrapping

Esta sección se trató algunos ejemplos de scripts desarrollados en Python y que trabajan con la librería BeautifulSoup para el manejo y extracción de información en páginas web.
Entre los scripts:
- [scrpe_quote.py]()
* [scrap1.py]()
+ [scrap2.py]()
- [scrap3.py]()
* [scrap4.py]()
+ [scrap5.py]()
- [scrap6.py]()
* [scrap7.py]()
+ [scrap8.py]()
- [scrap9.py]()
* [scrap10.py]()
+ [scrap11.py]()
- [scrap12.py]()

### scrape_quote.sh
Este script utiliza una página web llamada *Quotes to Scrape* la cual permite realizar pruebas de Webscrapping ofreciendo diversas alterativas de extracción de citas textuales de ciertos autores. Este script utiliza librerías de Python como **requests** para hacer conexión con la página y extraer su contenido mediante un response, y **BeautifulSoup** para el manejo de información de archivos HTML contenidos en el response. Esta última librería nos permitirá manejar la información y extraer citas textuales y autores que están contenidas dentro del código HTML de la página web, todo esto para guardarlas en listas y darles salida en un documento en Excel (.csv) donde se incluirá la cita y el autor que corresponde.

### scrape1.py
Este script página web llamada *Fake Jobs* la cual permite realizar pruebas de Webscrapping ya que esta página está conformada por anuncios de empleos. Este script importa la librería **requests** para realizar una conexión a la página mencionada, extrae la información HTML de la página y la imprime como texto plano en consola.

### scrape2.py
Utiliza como base el script *scrape1.py*, la diferencia es que ahora nuestro response será tratado. Importa la librería **requests** para realizar una conexión a la página *Fake Jobs*, extrae la información HTML de la página y mediante la librería **BeautifulSoup** analiza el contenido del HTML y lo va limitando a contenido que nos interesa en este caso reduciremos a los tags con *id=ResultsContainer* que es los que contienen la información que nos interesa e imprime la salida en consola. A diferencia del anterior veremos un resultado más reducido.

### scrape3.py
Este script utiliza como base el script *scrape2.py*, una vez que reducimos el contenido de la página buscando tags con *id=ResultsContainer* buscamos información a base de metadatos, por ejemplo, buscamos elementos de la clase *class=card-content"* los cuales contienen información que nos interesa.

### scrape4.py
Este script utiliza como base el script *scrape3.py*, una vez extraídos los datos con la clase *class=card-content* pasamos a darle formato a la información que se encuentra aqui, ahora nos centramos en buscar información en los títulos o textos que haya en la página, extraemos los textos que contengan clases como *class= title, company or location* el cual nos extrae información con el título del empleo, la compañía que ofrece el empleo y la localización del mismo. Los resultados se imprimen en consola, pero aun muestran tags de HTML.

### scrape5.py
Este script utiliza como base el script *scrape4.py*, como se menciona en el anterior script la información sigue mostrándose en HTML esto debido que al utilizar el método **find()** de Bs4 nos arroja código HTML, por lo que usaremos la propiedad **.text** en la variable que se guarda el resultado del método anterior. Así podremos mostrar el texto sin etiquetas HTML. El resultado es el mismo que el script anterior mostrando:
- El título del empleo
* La compañía que lo ofrece
+ Localización del empleo
Aunque lo muestra en crudo y aun no tiene un formato claro y arroja espacios en blanco.

### scrape6.py
Este script utiliza como base el script *scrape5.py*, 
como se menciona al final del anterior script el resultado sigue arrojando espacios en blanco por lo que a la variable que guarde la salida del método **find()** además de agregarle la propiedad **.text** también se le agregará el método **strip()** esto para ignorar los espacios en blanco extras. La salida se imprime en consola, de igual manera arroja: 
- El título del empleo
* La compañía que lo ofrece
+ Localización del empleo
Aunque aún sigue mostrando el texto y no queda muy claro que es lo que explica.

### scrape7.py
Este script utiliza como base el script *scrape3.py*, pero ahora buscamos trabajos que tengan que ver con *Python*, para esto utilizamos el método **find_all()** el cual busca mediante un texto (en este caso "Python") los trabajos que estén relacionados en la búsqueda hecha en *scrape3.py*. En la salida únicamente contamos los trabajos que están disponibles y se imprimen en pantalla la cantidad de ellos.

### scrape8.py
Este script utiliza como base el script *scrape7.py*, y combina la búsqueda del script *scrape4.py* en donde busca en los textos información que tenga la clase *class_=title, company, location* para extraer detalles de trabajos que tengan que ver con Python. Damos salida a los resultados en consola dándoles formato con la propiedad **.text** y la función **strip()** en la variable correspondiente resultante del método **find()** ya que recordemos que vienen con etiquetas HTML. Como podemos ver en la salida ocurre un error debido a que intentamos hacer búsquedas que no son permitidas ya que accedemos a niveles de anidamiento de tags que no existen. Para ello debemos diseñar un script para cada página a analizar.

### scrap9.py
Este script corrige los errores de *scrape8.py*, pues ahora en lugar de combinar la búsqueda de trabajos con el *scrape3.py* crea la suya y accede a los niveles correctos. Por lo que ahora la salida será correcta y arroja trabajos que tengan relación con Python.

### scrap10.py
Este script utiliza como base el script *scrape9.py*, solo que ahora agrega una búsqueda de links donde se pueda contactar el empleo y les da salida de la misma forma que el script anterior y dándoles formato con la propiedad **.text** y la función **strip()** a la variable resultante del método **find()** de bs4. 
La salida incluye:
- El título del empleo
* La compañía que lo ofrece
+ Localización del empleo
- Link para contactar a la empresa
Al darle salida podemos ver que no arroja los links correspondientes ya que el atributo **.text** correspondiente a la variable resultante del método **find()** elimina cualquier información extra incluidas referencias pues solo deja el texto.

### scrap11.py
Este script corrige los errores de *scrap10.py* pues lo usa como base, pero ahora los links los accede directamente al utilizar la función **.find_all()** y buscar cualquier etiqueta con links de referencias. Esto nos arroja una lista la cual iteraremos con un for y daremos salida en consola al link directamente de la lista como si fuese un string cualquiera guardado dentro.
Al ejecutar este script ahora si arrojará dos links uno de la página *Fake jobs* y el otro donde podremos contactar el supuesto empleo.

### scrap12.py
Este script usa *scrap11.py* y en la salida arroja solamente el link donde podremos contactar el supuesto empleo pues el otro no es de nuestro interés.
