#Script scrap10.py
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

python_jobs_elements= [h2_element.parent.parent.parent for h2_element in python_jobs]

for job_element in python_jobs_elements:
    title_element= job_element.find("h2", class_="title")
    company_element= job_element.find("h3", class_="company")
    location_element= job_element.find("p", class_="location")
    
    links= job_element.find_all("a")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    for link in links:
        link_url=link["href"]
        print(link.text.strip())
    print()