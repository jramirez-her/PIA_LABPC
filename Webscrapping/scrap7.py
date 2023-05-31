#Script scrap7.py
#21/03/2023-Joaquin Ramirez Hernandez
import requests
from bs4 import BeautifulSoup

#
##Obtencion de datos mediante peticion get
url= "https://realpython.github.io/fake-jobs/"
page= requests.get(url)

#
##Se analiza el contenido con bs4
soup= BeautifulSoup(page.content, "html.parser")
results= soup.find(id="ResultsContainer")

job_elements= results.find_all("div", class_="card-content")

python_jobs= results.find_all("h2", string=lambda text: "python" in text.lower())
print(len(python_jobs))