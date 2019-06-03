from bs4 import BeautifulSoup
import requests
import csv

edicoes = [1527, 1424, 1425, 1475]
num_gravados = 0

def webscrape(numeros):
    global num_gravados
    url = f'http://www.uel.br/revistas/uel/index.php/informacao/issue/view/{numeros}'
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    lidos = 0
   
    for texto in soup.find_all('table', class_='tocArticle'):
        titulo = texto.find('div', class_='tocTitle').text.strip().replace('\t', '')
        autor = texto.find('div', class_='tocAuthors').text.strip().replace('\t', '')
        print(f'Título do trabalho: {titulo}')
        print(f'Autores: {autor}')
        print()
        csv_writer.writerow([titulo, autor])
        lidos += 1
        num_gravados += 1
    return lidos > 0



# realiza operações com arquivos csv
arquivo_csv = open('InfoeInfo.csv', 'w', encoding='utf-8')
csv_writer = csv.writer(arquivo_csv)
csv_writer.writerow(['titulo', 'autor'])

for item in edicoes:
    webscrape(item)

arquivo_csv.close()

print(f'Total de registros gravados: {num_gravados}')

