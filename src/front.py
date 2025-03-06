import streamlit as st
import pandas as pd
import controller_filmes as ctrl

filmes = pd.read_csv("data/filmes_df.csv")
st.header("Recomendação de filmes")
filme_escolhido = st.selectbox("Escolha um filme: ", filmes['name'].values)

if st.button("Descubra novos filmes similares: "):
    filmes, posteres = ctrl.recomendar(filme_escolhido)
    lista_filmes = filmes.tolist()
    lista_posteres = posteres.tolist()
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.markdown(lista_filmes[0])
        st.image(lista_posteres[0], width=400)
    with col2:
        st.text(lista_filmes[1])
        st.image(lista_posteres[1], width=400)
    with col3:
        st.text(lista_filmes[2])
        st.image(lista_posteres[2], width=400)
    with col4:
        st.text(lista_filmes[3])
        st.image(lista_posteres[3], width=400)
    with col5:
        st.text(lista_filmes[4])
        st.image(lista_posteres[4], width=400)
    
        