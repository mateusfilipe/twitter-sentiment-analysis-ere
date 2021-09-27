# Executar o comando abaixo para instalar a biblioteca de snscrape.git
#!pip install git+https://github.com/JustAnotherArchivist/snscrape.git

# Executar comando abaixo caso não tenha Pandas instalado
#!pip install pandas

import os
import pandas as pd

# Configurando quantidade de tweets limites a serem coletados
tweet_count = 5000

#Configurando palavras chaves para serem pesquisadas na base de dados do twitter
text_query = ("IFMG" or "IFMG Sabara" or 
             "IF Sabara" or "Sabara IF" or 
             "IF Sabara" or "ERE" or
             "Ensino Remoto" or "EAD IF" or
             "ERE IF" or "IF ERE" or
             "Ensino Remoto Emergencial")

#Primeira coleta, expectativa para ERE - junho/julho/agosto - 2020
since_date1 = "2020-06-01"
until_date1 = "2020-08-31"

#Segunda coleta, avaliacao do ERE - setembro/outubro/novembro - 2020
since_date2 = "2020-09-01"
until_date2 = "2020-11-30"

#Terceira coleta, avaliacao do ERE - fevereiro/marco/abril- 2021
since_date3 = "2021-02-01"
until_date3 = "2021-04-30"

#Quarta coleta, expectativa para volta da aula presencial - maio/junho-julho - 2021
since_date4 = "2021-05-01"
until_date4 = "2021-07-31"

# Using OS library to call CLI commands in Python
os.system('snscrape --jsonl --max-results {} --since {} twitter-search "{} until:{} lang:pt"> text-query-tweets.json'.format(tweet_count, since_date4, text_query, until_date4))

# Reads the json generated from the CLI command above and creates a pandas dataframe
tweets_df2 = pd.read_json('text-query-tweets.json', lines=True)

# Displays first 5 entries from dataframe
tweets_df2.head()

# Exportar os dados para uma planilha .csv
# tweets_df2.to_csv('Coleta1_Expectativa1.csv', sep=',', index=False)
# tweets_df2.to_csv('Coleta2_Avaliacao1.csv', sep=',', index=False)
# tweets_df2.to_csv('Coleta3_Avaliacao2.csv', sep=',', index=False)
tweets_df2.to_csv('Coleta4_Expectativa2.csv', sep=',', index=False)
