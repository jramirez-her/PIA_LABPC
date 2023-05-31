#Script scrap1.py
#21/03/2023-Joaquin Ramirez Hernandez
import requests

url= "https://realpython.github.io/fake-jobs/"
page= requests.get(url)

print(page.text)