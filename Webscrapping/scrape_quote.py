#Script scrape_quote.py
#21/03/2023-Joaquin Ramirez Hernandez
import requests
import csv
from bs4 import BeautifulSoup

url="http://quotes.toscrape.com/"
response= requests.get(url)
#
##Analizar el html
html=BeautifulSoup(response.text, 'html.parser')
#Extraer citas y autores del archivo html
quotes_html= html.find_all('span', class_="text")
authors_html= html.find_all('small', class_="author")
#
##Citas en forma de lista
quotes=list()
for quote in quotes_html:
    quotes.append(quote.text)
#
##Autores en forma de lista
authors= list()
for author in authors_html:
    authors.append(author.text)

for t in zip(quotes, authors):
    print(t)
#
##Guardar en el directorio actual
with open('./citas_1860939.csv', 'w') as csv_file:
    csv_writer= csv.writer(csv_file, dialect='excel')
    csv_writer.writerows(zip(quotes, authors))