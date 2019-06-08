from bs4 import BeautifulSoup
import requests
import csv
import re

edicoes = [1527]
links = []
issues_gravados = 0
articles_gravados = 0 

def webscrape_issues(numeros):
    global issues_gravados
    url = f'http://www.uel.br/revistas/uel/index.php/informacao/issue/view/{numeros}'
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    lidos = 0
   
    for texto in soup.find_all('table', class_='tocArticle'):
        link = texto.find('a', attrs={'href': re.compile("http://")})
        link2 = str(link.get('href')[65:70])
        titulo = texto.find('div', class_='tocTitle').text.strip()
        autor = texto.find('div', class_='tocAuthors').text.strip().replace('\t', '')
        pages = texto.find('div', class_='tocPages').text.strip().replace('\t', '')
        if autor is not '' and pages is not 'i':
            links.append(link2)
        print(f'Título do trabalho: {titulo}')
        print(f'Autores: {autor}')
        print(f'Link: {link2}')
        print(f'Páginas: {pages}')
        print()
        lidos += 1
        issues_gravados += 1
    return lidos > 0

def webscrape_articles(numeros):
    global articles_gravados
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
        csv_writer.writerow([titulo, autor, resumo, keywords])
        lidos += 1
        articles_gravados += 1
    return lidos > 0

#realiza operações com arquivos csv
arquivo_csv = open('InfoeInfov2.csv', 'w', encoding='utf-8')
csv_writer = csv.writer(arquivo_csv)
csv_writer.writerow(['titulo', 'autor','resumo','keywords'])

for item in edicoes:
    webscrape_issues(item)

print(f'Total de artigos analisados: {issues_gravados}')
print(links)
for item in links:
    webscrape_articles(item)

arquivo_csv.close()
print(f'Total de artigos reunidos: {articles_gravados}')




