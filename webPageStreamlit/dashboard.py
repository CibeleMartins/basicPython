import streamlit as st

st.header("Dashboard")
st.sidebar.text("Escolha o que deseja filtrar")

# exibicao de dados

import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.rand(10, 3),
    columns= ['Ação', 'Aventura', 'Terror']
)


# table o dataframe criam uma tabela
# dataframe da a possibilidade de aumentar ou diminuir as colunas
st.dataframe(df)
st.table(df)


st.line_chart(df)