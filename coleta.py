from datetime import datetime

from coinbase10 import consultar_preco
from banco import criar_tabela, inserir_preco
import time
criar_tabela()

moedas = ["BTC-USD", "ETH-USD", "SOL-USD"]
# automaçao

while True:
    for moeda in moedas:

        dados = consultar_preco(moeda)

        preco = float(dados["data"]["amount"])

        data_hora = datetime.now()

        inserir_preco(moeda, preco, data_hora)

        print("dados coletados com sucesso")

        print("Moeda:",moeda)
        print("Preço:",preco)
        print("Data e hora:",data_hora)

        print ("Todas as moeda foram coletadas com sucesso!")


    time.sleep(60)



