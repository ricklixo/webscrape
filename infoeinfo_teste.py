from bs4 import BeautifulSoup
import requests
import csv
import re

edicoes = [1527]
links = []
num_gravados = 0

def webscrape_edicoes(numeros):
    global num_gravados
    url = f'http://www.uel.br/revistas/uel/index.php/informacao/issue/view/{numeros}'
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    lidos = 0
   
    for texto in soup.find_all('table', class_='tocArticle'):
        link = texto.find('div', class_='tocTitle').a
        link2 = link['href']
        titulo = texto.find('div', class_='tocTitle').text.strip()
        autor = texto.find('div', class_='tocAuthors').text.strip().replace('\t', '')
        print(f'Título do trabalho: {titulo}')
        print(f'Autores: {autor}')
        print(f'Link: {link2}')
        print()
        lidos += 1
        num_gravados += 1
    return lidos > 0

for item in edicoes:
    webscrape_edicoes(item)

print(links)

print(f'Total de artigos analisados: {num_gravados}')

