# 🎬 Recomendador de Filmes com Python

Este projeto é um script em Python que te recomenda filmes aleatórios diretamente do site [Letterboxd](https://letterboxd.com), usando **web scraping** com `requests` e `BeautifulSoup`.

Você pode escolher entre:
- Receber recomendações aleatórias de filmes populares.
- Receber recomendações da sua própria **watchlist** do Letterboxd.

## 📌 Funcionalidades

- Acesso à página de filmes populares do Letterboxd.
- Busca na watchlist de um usuário (se estiver pública).

## 🛠️ Tecnologias utilizadas

- Python 3.
- [requests](https://pypi.org/project/requests/)
- [BeautifulSoup (bs4)](https://pypi.org/project/beautifulsoup4/)

## ▶️ Como executar

1. Clone o repositório:
  ```
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd recomendador-de-filme
  ```
2. Crie e ative um ambiente virtual (opcional, mas recomendado):
```
python -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate
```
3. Instale as dependências:
```
pip install -r requirements.txt
```
4. Execute o script:

```
python main.py
```
