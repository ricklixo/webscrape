from bs4 import BeautifulSoup
import requests
import csv

num_gravados = 0

def save_pagina(item):
    global num_gravados
    num_lidos = 0
    url = 'http://serious.gameclassification.com/EN/games/index.html?display=taxonomy&sort=game_year%20ASC&start={}'
    source = requests.get(url.format(item)).text
    print(item)
    soup = BeautifulSoup(source, 'html')

    for row in soup.find_all('tr'): # Como tem esse problema da classe, pegue todas!
        if not 'table_title' in row.attrs['class']: # se a tabela 'table_title não estiver em 'class'
            # operações com as tabelas - verifica as tags TD, que são as colunas.
            tab1 = row.find_all('td')

            # Aqui eu crio variáveis correspondentes às colunas que eu desejo verificar. O método strip() serve para remover os espaços em branco.
            titulo1 = tab1[0].text.strip() # coluna NOME
            ano1 = tab1[1].text.strip()    # coluna ANO
            proposta1 = tab1[3].text.strip() # coluna PROPOSTA
            mercado1 = tab1[4].text.strip()  # coluna MERCADO ALVO

            # Aqui imprimo os resultados finais que serão exportados para um .csv - APENAS CHECAGEM
            #print('Título: {}'.format(titulo1))
            #print('Ano de lançamento: {}'.format(ano1))
            #print('Proposta Geral: {}'.format(proposta1))
            #print('Mercado Alvo: {}'.format(mercado1))
            #print()

            # escreve as informações alternadamente no arquivo, era a única forma de gravar em apenas um utilizando o loop duplo.
            csv_writer.writerow([titulo1, ano1, proposta1, mercado1])
            num_lidos += 1
            num_gravados += 1
    return num_lidos > 0

# Realiza operações com arquivos .csv
arquivo_csv = open('lista_serious.csv', 'w')
csv_writer = csv.writer(arquivo_csv)
csv_writer.writerow(['Título', ' Ano', ' Proposta', ' Mercado'])

# operações referentes ao loop da página
item = 0
while save_pagina(item):
    item += 48
arquivo_csv.close()
print('Total de registros: %d' % num_gravados)
