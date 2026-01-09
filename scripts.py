import random
import requests
from bs4 import BeautifulSoup
import sys
import re
import os
from dotenv import load_dotenv
import requests

load_dotenv() 

def get_poster_tmdb(movie_title, year=None):
    API_KEY = os.getenv("TMDB_API_KEY")
    base_url = "https://api.themoviedb.org/3/search/movie"

    params = {
        "api_key": API_KEY,
        "query": movie_title,
        "year": year
    }

    try:
        response = requests.get(base_url, params=params, timeout=5000,)
        response.raise_for_status()  # valida erro HTTPs
        data = response.json()

        if data.get("results"):
            poster_path = data["results"][0].get("poster_path")
            if poster_path:
                return f"https://image.tmdb.org/t/p/w500{poster_path}"

    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar poster no TMDB: {e}")

    return None  # fallback


def getMovieList(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        list = soup.select('div.react-component')
        movies = []
        for movie in list:
            title = movie.get('data-item-name')
            link = movie.get('data-item-link')
            if title and link:
                url = "https://letterboxd.com" + link
                year = re.sub('[^0-9]', '', title)
                movies.append({
                    "title": title,
                    "url": url,
                    "year": year,
                    "img": "",
                })
        return movies
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao acessar {url}: {e}")
        return []

def getByWatchlist(username):
    return f'https://letterboxd.com/{username}/watchlist/'

def getUrl():
    return f'https://letterboxd.com/films/ajax/page/{random.randint(0,5)}'


def getMovie(movielist):
    index = random.randint(0, len(movielist) - 1)
    filme = movielist.pop(index)
    text_only = filme['title'].split(' (')[0]
    filme['img'] = get_poster_tmdb(text_only , filme['year'])
    return filme, movielist

def ask(msg):
    res = ''
    while res not in ['Y','N']:
        res = input(f"{msg}(Y/N)").upper()
    return res == 'Y' # retorna True se for Y, False se for N
           
def recomendar(movielist):
    while movielist: # enquanto houver filmes na lista
        filme, movielist = getMovie(movielist)
        if __name__ != "__main__":
            return filme, movielist
        print(f"\nFilme: {filme['title']}\nAcesse:{filme['url']}\nPoster: {filme['img']}\n")
        if(ask("Você vai assistir esse filme? Se não vou te recomendar outro!")):
            print("Bom filme")
            sys.exit() 
    
        
def popularmovies ():
    movielist = getMovieList(getUrl())
    if __name__ != "__main__":
        return movielist
    while True:
        if not movielist:
            if(ask("Ja te recomendei varios filmes, tem certeza que quer assistir filme? Se sim vou continuar te recomendando!")):
                movielist = getMovieList(getUrl())
            else:
                print("Fica pra proxima!")
                sys.exit() 
        else:
            recomendar(movielist)
        
    
def watchlist ():
    print("Atenção! Essa opção funciona apenas se: \n1.Você tiver uma conta no Letterboxd.\n2.Sua Watchlist estiver pública e com filmes adicionados.")
    username = input('Informe o username: ').strip()
    movielist = getMovieList(getByWatchlist(username))
    if not movielist:
        print("Não foi possível acessar a watchlist. Verifique o nome de usuário ou a visibilidade da lista.")
    else:
        while True:
            recomendar(movielist)
            if not movielist:
                if(ask("Já recomendei todos os filmes da sua watchlist. Deseja ver sugestões aleatórias?")):
                    movielist = getMovieList(getUrl())
                else:
                    print("Fica pra proxima!")
                    sys.exit() 
def menu():
    print("Recomendador de Filmes")
    print(f"Opções:\n1. Receber sugestão aleatória\n2. Receber sugestão da minha Watchlist (Letterboxd)\n3. Sair")
    res = ''
    while res not in ['1', '2','3']:
        res=input("Escolha o número da opção: ")
    if(res == '1'):
        popularmovies()
    elif(res == '2'):
        watchlist()
    elif(res == '3'):
        print('saindo...')
        sys.exit() 

if __name__ == "__main__":
    menu()

