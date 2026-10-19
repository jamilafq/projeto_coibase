import streamlit as st
import pandas as pd
import sqlite3

st.set_page_config( page_title= "Dashboard-Coinbase", page_icon= "$", layout= "wide")

st.title("Dashboard de criptoMoedas")

st.write("Visualização dos dados coletados da API da CoinBase")

 #atualizaçao automatica


@st.cache_data(ttl=60)


#funçao do python

def carregar_dados():
    conexao = sqlite3.connect("coinbase5.db") 
    try: 
        df =pd.read_sql_query("SELECT moeda, preco, data_hora FROM precos  ORDER BY data_hora",
                              conexao,)
    finally:
        conexao.close()  

    df["data_hora"]= pd.to_datetime(df["data_hora"])
    df["preco"] =   pd.to_numeric(df["preco"], errors= "coerce")  

    return df    

try: 
    df= carregar_dados()

except Exception as erro:
    st.error(f"Não foi possível le o banco de dados : {erro}")
    st.stop()
if df.empty:
    st.warning("ainda nao xistem dados no banco")    
    st.stop ()

#começa a parte de visualização

moedas = df ["moeda"].unique() #seleciona refere-se à identificação e ao isolamento de itens que não se repetem 

for coluna, moeda in zip(st.columns(len(moedas)), moedas):
    precos= df.loc[df["moeda"] == moeda,"preco"]

    atual= precos.iloc[-1]
    anterior = precos.iloc[-2] if len (precos) > 1 else None
    delta = f"{atual-anterior:.2f}" if anterior is not None else None

    with coluna:
        st.metric(moeda,f"${atual:.2f}", delta=delta)
        st.write(f"Maior preço:${precos.max():2f}")
        st.write(f"Menor preço:${precos.min():.2f}")
        st.write(f"Media:${precos.mean():,.2f}")
        st.write(f"amplitude:${precos.max()-precos.min():,.2f}")
# Analise detalhadas 
st.subheader ("Análise da Critomoeda")  
moeda_selecionada = st.selectbox("selecione a criptomoeda desejada para analise ",moedas)
dados_moeda = df [df["moeda"]== moeda_selecionada]
st.subheader (f"Historico de preço -{moeda_selecionada}")
st.line_chart(dados_moeda.set_index("data_hora")["preco"])

st.divider()
st.subheader(F"dados coletaos -{moeda_selecionada}")

st.dataframe(dados_moeda)
