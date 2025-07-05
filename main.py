import random
import requests
from bs4 import BeautifulSoup
import sys

def getMovieList(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.select('li.poster-container')
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao acessar {url}: {e}")
        return []

def getByWatchlist(username):
    return f'https://letterboxd.com/{username}/watchlist/'

def getUrl():
    return f'https://letterboxd.com/films/ajax/page/{random.randint(0,20)}'


def getMovie(movielist):
    index = random.randint(0, len(movielist) - 1)
    filme = movielist[index]
    title = filme.img.get('alt')
    poster_div = filme.find('div', class_='film-poster')
    url = "https://letterboxd.com/film/" + poster_div.get('data-film-slug')
    del movielist[index]
    return title, url

def ask(msg):
    res = ''
    while res not in ['Y','N']:
        res = input(f"{msg}(Y/N)").upper()
    return res == 'Y' # retorna True se for Y, False se for N
           
def recomendar(movielist):
    while movielist: # enquanto houver filmes na lista
        title, url = getMovie(movielist)
        print(f"\nFilme: {title}\nAcesse:{url}\n")
        if(ask("Você vai assistir esse filme? Se não vou te recomendar outro!")):
            print("Bom filme")
            sys.exit() 
    
        
def popularmovies ():
    movielist = getMovieList(getUrl())
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

