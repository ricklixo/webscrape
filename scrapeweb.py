from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

# source = requests.get('http://serious.gameclassification.com/EN/games/index.html?display=taxonomy').text
url = 'http://serious.gameclassification.com/EN/games/index.html?display=taxonomy&sort=game_year%20ASC'
source = requests.get(url).text
soup = BeautifulSoup(source, 'lxml')

# operações para escrever em um arquivo .csv
csv_file1 = open('lista_serious1.csv', 'w')
csv_file2 = open('lista_serious2.csv', 'w')

csv_writer1 = csv.writer(csv_file1)
csv_writer1.writerow(['Título ', 'Ano ', 'Proposta ', 'Mercado '])

csv_writer2 = csv.writer(csv_file2)
csv_writer2.writerow(['Título ', 'Ano ', 'Proposta ', 'Mercado '])

# Como o site possui duas numerações de tabelas, criei 2 loops.
for tabela1 in soup.find_all('tr', class_='table_item_1'):
    # operações com as tabelas - verifica as tags TD, que são as colunas.
    tab1 = tabela1.find_all('td')

    # Aqui eu crio variáveis correspondentes às colunas que eu desejo verificar. O método strip() serve para remover os espaços em branco.
    titulo1 = tab1[0].text.strip()
    ano1 = tab1[1].text.strip()
    proposta1 = tab1[3].text.strip()
    mercado1 = tab1[4].text.strip()

    record1.append([titulo1, ano1, proposta1, mercado1])

    # Aqui imprimo os resultados finais que serão exportados para um .csv
    print('Título: {}'.format(titulo1))
    print('Ano de lançamento: {}'.format(ano1))
    print('Proposta Geral: {}'.format(proposta1))
    print('Mercado Alvo: {}'.format(mercado1))
    print()
    csv_writer1.writerow([titulo1, ano1, proposta1, mercado1])

print(record1)
df = pd.DataFrame(record1, columns=['Titulo', 'ano', 'proposta', 'mercado'])
print(df.head())

csv_file1.close()






