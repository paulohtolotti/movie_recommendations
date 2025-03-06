import streamlit as st
import pandas as pd
import controller_filmes as ctrl

filmes = pd.read_csv("data/filmes_df.csv")
st.header("Recomendação de filmes")
filme_escolhido = st.selectbox("Escolha um filme: ", filmes['name'].values)

if st.button("Descubra novos filmes similares: "):
    recomendacoes = ctrl.recomendar(filme_escolhido)

    for filme in recomendacoes:
        st.write(filme)