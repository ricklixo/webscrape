from bs4 import BeautifulSoup
import requests
import csv

edicoes = [34617]
num_gravados = 0

def webscrape(numeros):
    global num_gravados
    url = f'http://www.uel.br/revistas/uel/index.php/informacao/article/view/{numeros}'
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    lidos = 0
   
    for texto in soup.find_all('div', id='content'):
        titulo = texto.find('div', id='articleTitle').text.strip()
        autor = texto.find('div', id='authorString').text.strip()
        resumo = texto.find('div', id='articleAbstract').text.strip().replace('Resumo', '').replace('\n', '')
        keywords = texto.find('div', id='articleSubject').text.strip().replace('Palavras-chave', '').replace('\n', '')
        print(f'Título do trabalho: {titulo}')
        print(f'Autores: {autor}')
        print(f'Resumo: {resumo}')
        print(f'Palavras-Chave: {keywords}')
        print()
        #csv_writer.writerow([titulo, autor])
        lidos += 1
        num_gravados += 1
    return lidos > 0



# realiza operações com arquivos csv
arquivo_csv = open('InfoeInfoArticles.csv', 'w', encoding='utf-8')
csv_writer = csv.writer(arquivo_csv)
csv_writer.writerow(['titulo', 'autor'])

for item in edicoes:
    webscrape(item)

arquivo_csv.close()
print(f'Total de registros gravados: {num_gravados}')