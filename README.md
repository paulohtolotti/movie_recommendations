# API de Recomendação de Filmes

Este projeto é uma API de recomendação de filmes desenvolvida com Flask. A API recebe o nome de um filme e retorna uma lista de filmes semelhantes com base em uma matriz de similaridade.

## Tecnologias Utilizadas
- Python
- Streamlit
- Flask
- Pandas
- Pickle (para carregar a matriz de similaridade)

## Estrutura do Projeto
```
recomendacao_filmes/
│── app_api.py  # Arquivo principal da API
│── modelo.py  # Arquivo com a lógica de recomendação
│── front.py  # Arquivo front-end da aplicação
│── data/
│   ├── filmes_df.csv  # Dataset dos filmes
│   ├── matriz_similaridade.pkl  # Matriz de similaridade
│── requirements.txt  # Dependências
```

## Instalação
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/recomendacao-filmes.git
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd recomendacao-filmes
   ```
3. Crie um ambiente virtual e ative:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Executando a API
1. Inicie a API:
   ```bash
   python app_api.py
   ```
2. A API estará rodando em `http://127.0.0.1:5000`

## Como Usar
Para obter recomendações de um filme, faça uma requisição GET para:
```
http://127.0.0.1:5000/recomendar?filme=Nome%20do%20Filme
```
Exemplo:
```
http://127.0.0.1:5000/recomendar?filme=Goodfellas
```
### Resposta Esperada
```json
{
    "filme": "Goodfellas",
    "recomendacoes": ["Filme1", "Filme2", "Filme3", "Filme4", "Filme5"]
}
```

## Testando com `curl`
```bash
curl "http://127.0.0.1:5000/recomendar?filme=Goodfellas"
```

## Testando com Python
```python
import requests

url = "http://127.0.0.1:5000/recomendar?filme=Goodfellas"
resposta = requests.get(url)
print(resposta.json())
```

## Contribuição
Sinta-se à vontade para abrir issues e enviar pull requests para melhorar o projeto.

## Licença
Este projeto está sob a licença MIT.

