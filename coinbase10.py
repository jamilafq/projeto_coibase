import requests


def consultar_preco(moeda):
    url = f"https://api.coinbase.com/api/v2/prices/{moeda}/spot"

    resposta = requests.get(url)

    dados = resposta.json()

    return dados



