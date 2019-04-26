from bs4 import BeautifulSoup
import requests
import csv

num_gravados = 0 #serve para mostra no final quantos registros foram gravados.

def web_scrape(item): # cria uma função chamada webscrape - BOAS PRÁTICAS.
    global num_gravados # declara a variável como global, para ser usada fora da função
    num_lidos = 0 #serve para mostrar quandos registros foram lidos
    url = 'http://serious.gameclassification.com/EN/games/index.html?start={}&sort=game_year%20ASC&display=taxonomy'.format(item) # utilizo a variável item para buscar o numero de queries por página
    source = requests.get(url).text
    print(item)
    soup = BeautifulSoup(source, 'lxml')

    # Tive que criar um loop FOR duplo, já que a class se repete alternadamente e não estava conseguindo pegar os dados.
    for tabela in soup.find_all('tr'):
        if not 'table_title' in tabela.attrs['class']: # eu verifico todas, MENOS as que são 'class = 'table_title'
            tab1 = tabela.find_all('td')
            # Aqui eu crio variáveis correspondentes às colunas que eu desejo verificar. O método strip() serve para remover os espaços em branco.
            titulo = tab1[0].text.strip() # coluna NOME
            ano = tab1[1].text.strip()    # coluna ANO
            proposta = tab1[3].text.strip() # coluna PROPOSTA
            mercado = tab1[4].text.strip()  # coluna MERCADO ALVO

            # Aqui imprimo os resultados finais que serão exportados para um .csv - APENAS CHECAGEM
            #print('Título: {}'.format(titulo))
            #print('Ano de lançamento: {}'.format(ano))
            #print('Proposta Geral: {}'.format(proposta))
            #print('Mercado Alvo: {}'.format(mercado))
            #print()
            csv_writer.writerow([titulo, ano, proposta, mercado])
            num_lidos += 1 
            num_gravados += 1
    return num_lidos > 0 # O return vai indicar se ele conseguiu ler alguma linha na página. Se a rotina não traz nenhum novo registro, então quer dizer que chegou no final.

# Realiza operações com arquivos .csv
arquivo_csv = open('lista_serious_games.csv', 'w', encoding='utf-8') # o encoding UTF8 é essencial para salvar
csv_writer = csv.writer(arquivo_csv)
csv_writer.writerow(['Título', ' Ano', ' Proposta', ' Mercado'])

# Realiza o loop de verificação na página.
item = 0 # essa variável ser para verificar o número de buscas das urls.
while web_scrape(item):
    item += 48

arquivo_csv.close()
print('Total de registros gravados: {}'.format(num_gravados))