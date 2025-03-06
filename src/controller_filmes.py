#imports
import pickle
import pandas as pd

#Dataframe de filmes
filmes_df = pd.read_csv("data/filmes_df.csv")
#Matriz similaridade
with open("data/matriz_similaridade.pkl", "rb") as f:
    matriz_cosseno = pickle.load(f)

def recomendar(nome):
    serie_indice = pd.Series(filmes_df.index, index=filmes_df['name'])
    serie_indice = serie_indice[~serie_indice.index.duplicated(keep="last")]

    filme_indice = serie_indice[nome]

    score_similaridade = pd.DataFrame(matriz_cosseno[filme_indice], columns=['score'])
    indices_recomendados = score_similaridade.sort_values('score', ascending=False)
    indices_recomendados = indices_recomendados[indices_recomendados['score'] > 0.5][1:6].index
    nomes = filmes_df['name'].iloc[indices_recomendados]
    posters = filmes_df['poster'].iloc[indices_recomendados]

    return nomes, posters

print(recomendar("The Dark Knight"))

