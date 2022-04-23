# import bibliotecas
from requests import Request, Session
import json
import pandas as pd
import os
import dotenv

dotenv.load_dotenv()
# API
pd.set_option("display.max_columns", None)
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': os.getenv('MARKETCAP')  # oculta a minha key no bot final
} 
session = Session()
session.headers.update(headers)

# função que pega as informações da moeda
def tipo_moeda(lista_moedas):
    # lista_dados_moedas = []
    for i in lista_moedas:
        moeda = {
            'slug': i,
            'convert': 'BRL'
            }
            
        # fazendo a requisição da API
        response_moeda_real = session.get(url, params=moeda)
        moeda_real = json.loads(response_moeda_real.text)
        print(moeda_real)
    
        # tratando dados do id da moeda
        id_moeda = moeda_real['data']
        id_moeda = list(id_moeda.keys())
        id_moeda = str(id_moeda)
        id_moeda = id_moeda.strip("[]'")
        # print(id_moeda)

        # selecionando o que a função irá retornar
        dados_moeda = moeda_real['data'][id_moeda]
        # esta_ativa                  = dados_moeda['is_active']
        sigla_moeda                 = dados_moeda['symbol']
        nome_moeda                  = dados_moeda['name']
        cotacao_moeda               = dados_moeda['quote']['BRL']['price']
        cap_mercado                 = dados_moeda['quote']['BRL']['market_cap']
        fornecimento_circulante     = dados_moeda['total_supply']
        # variacao_porcentagem_1h     = dados_moeda['quote']['BRL']['percent_change_1h']
        # variacao_porcentagem_24h    = dados_moeda['quote']['BRL']['percent_change_24h']
        # variacao_porcentagem_7_dias = dados_moeda['quote']['BRL']['percent_change_7d']
        # print(nome_moeda)
        # lista_dados_moedas.append([sigla_moeda, nome_moeda, cotacao_moeda, cap_mercado, fornecimento_circulante])
        # x = pd.DataFrame(lista_dados_moedas, columns=['Sigla','Nome', 'Cotação', 'Capitalização de Mercado', 'Fornecimento'])
        y =(f"Sigla: {sigla_moeda}\nNome: {nome_moeda}\nCotação: R$ {cotacao_moeda}\nCapitalização de Mercado: R$ {cap_mercado}\nFornecimento Circulante: {fornecimento_circulante}")
        
        
    return y

lista_moeda = ['ethereum']
tipo_moeda(lista_moeda)
# tabela_cripto = pd.DataFrame(tipo_moeda(lista_moeda), columns=['Sigla', 'Nome', 'Cotação', 'Cap de mercado', 'Fornecimento circulante'])
# tabela_cripto.style.format({'Cotação': '$ {:,.2f}', 'Cap de mercado': '$ {:.5f}', 'Fornecimento circulante': '{:,.0f}'})

# print(tabela_cripto)

# transformando em uma lista
# lista_moedas =['bitcoin']
# print(tipo_moeda(lista_moedas))