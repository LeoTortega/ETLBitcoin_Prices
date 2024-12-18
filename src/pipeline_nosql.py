import requests
from datetime import datetime
from tinydb import TinyDB
import time

def extract_dados_bitcoin():
    url = 'https://api.coinbase.com/v2/prices/spot'

    response = requests.get(url)
    dados = response.json()

    return dados

def transform_dados_bitcoin(dados):
    valor = dados['data']['amount']
    criptomoeda = dados['data']['base']
    moeda = dados['data']['currency']
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    dados_transformados = {
        'valor': valor,
        'criptomoeda': criptomoeda,
        'moeda': moeda,
        'timestamp': timestamp
    }

    return dados_transformados

def salvar_dados_tiny_db(dados, db_name="bitcoin.json"):
    db = TinyDB(db_name)
    db.insert(dados)

    print("Dados salvos com sucesso")

def main():
    while True:
        # Extração de dados
        dados_json = extract_dados_bitcoin()

        # Transformação de dados
        dados_map = transform_dados_bitcoin(dados_json)
        
        # Load de dados
        salvar_dados_tiny_db(dados_map)

        time.sleep(15)

if __name__ == '__main__':
    main()