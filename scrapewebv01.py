from bs4 import BeautifulSoup
import requests
import csv




url = 'http://serious.gameclassification.com/EN/games/index.html?display=taxonomy&sort=game_year%20ASC'
source = requests.get(url).text
soup = BeautifulSoup(source, 'lxml')

# Realiza operações com arquivos .csv
arquivo_csv = open('lista_serious.csv', 'w')
csv_writer = csv.writer(arquivo_csv)
csv_writer.writerow(['Título', ' Ano', ' Proposta', ' Mercado'])


# Tive que criar um loop FOR duplo, já que a class se repete alternadamente e não estava conseguindo pegar os dados.
for table in soup.find_all('div', class_='block_center_bottom'):
    for tabela1 in soup.find_all('tr', class_='table_item_1'): # Essa classe se repete alternadamente entre a tabela.

        # operações com as tabelas - verifica as tags TD, que são as colunas.
        tab1 = tabela1.find_all('td')

        # Aqui eu crio variáveis correspondentes às colunas que eu desejo verificar. O método strip() serve para remover os espaços em branco.
        titulo1 = tab1[0].text.strip() # coluna NOME
        ano1 = tab1[1].text.strip()    # coluna ANO
        proposta1 = tab1[3].text.strip() # coluna PROPOSTA
        mercado1 = tab1[4].text.strip()  # coluna MERCADO ALVO

        # Aqui imprimo os resultados finais que serão exportados para um .csv - APENAS CHECAGEM
        print('Título: {}'.format(titulo1))
        print('Ano de lançamento: {}'.format(ano1))
        print('Proposta Geral: {}'.format(proposta1))
        print('Mercado Alvo: {}'.format(mercado1))
        print()

        # escreve as informações alternadamente no arquivo, era a única forma de gravar em apenas um utilizando o loop duplo.
        csv_writer.writerow([titulo1, ano1, proposta1, mercado1])

    for tabela2 in soup.find_all('tr', class_='table_item_2'): # Essa classe se repete alternadamente entre a tabela.
        tab2 = tabela2.find_all('td')

        titulo2 = tab2[0].text.strip()
        ano2 = tab2[1].text.strip()
        proposta2 = tab2[3].text.strip()
        mercado2 = tab2[4].text.strip()

        print('Título: {}'.format(titulo2))
        print('Ano de lançamento: {}'.format(ano2))
        print('Proposta Geral: {}'.format(proposta2))
        print('Mercado Alvo: {}'.format(mercado2))
        print()

        csv_writer.writerow([titulo2, ano2, proposta2, mercado2])

arquivo_csv.close()
