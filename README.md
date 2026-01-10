# 🎬 Recomendador de Filmes com Python

Um site que recomenda filmes aleatórios ou baseado na sua watchlist pessoal do [Letterboxd](https://letterboxd.com). O projeto utiliza **web scraping** com `BeautifulSoup` para coletar dados do Letterboxd e a API do [TMDB](https://www.themoviedb.org) para buscar os posters dos filmes.

## ✨ Funcionalidades

- 🎲 **Filme Aleatório**: Recomenda um filme aleatório dos mais populares do Letterboxd
- 📋 **Watchlist Personalizada**: Recomenda filmes da sua watchlist do Letterboxd (perfil público)
- 🖼️ **Posters**: Exibe os posters dos filmes através da API do TMDB
- ⏱️ **Rate Limiting**: Proteção contra requisições excessivas
- 📱 **Interface Responsiva**: Design moderno e intuitivo


## 🚀Teste agora mesmo!!
Acesse a versão online: https://recomendador-de-filme-beige.vercel.app

## 🛠️ Tecnologias Utilizadas

- **Python 3.13+** - Linguagem principal
- **Flask** - Framework web
- **BeautifulSoup4** - Web scraping
- **Flask-Limiter** - Rate limiting
- **Requests** - Requisições HTTP
- **TMDB API** - Banco de dados de filmes
## ▶️ Instalação e Execução
 ### 📋 Pré-requisitos

- Python 3.10 ou superior
- Pip (gerenciador de pacotes do Python)
- Uma chave de API do [TMDB](https://www.themoviedb.org/settings/api) _somente para versão site_
### versão Web
1. Clone o projeto
```bash
git clone https://github.com/seu-usuario/recomendador-de-filme.git
cd recomendador-de-filme
```
2. Criar e Ativar Ambiente Virtual (Recomendado)

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

3. Instalar Dependências

```bash
pip install -r requirements.txt
```
4. Obtenha a API KEY no site [TMDB](https://www.themoviedb.org)
5. Crie um arquivo `.env` na raiz do projeto:

```env
TMDB_API_KEY=sua_chave_api_aqui
```

6. Executar a Aplicação

```bash
python main.py
```

A aplicação estará disponível em `http://localhost:5000`

## Versão CLI (Terminal)
  A versão CLI não requer a API do TMDB e roda diretamente no terminal.
1. Siga os passos 1-3 da versão web (clone, ambiente virtual, dependências)
2. Execute o script

 ```bash
python scripts.py
```
3. **Interaja com o menu no terminal** e aproveite as recomendações! 🍿

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se livre para solicitar pull request ou abre uma issue!

## 📝 Licença

Este projeto está licenciado sob a [MIT License](https://github.com/LeticiaParreiras/recomendador-de-filme/main/LINCENSE)

## 👨‍💻 Autor

Desenvolvido com ❤️ por Leticia Parreiras

