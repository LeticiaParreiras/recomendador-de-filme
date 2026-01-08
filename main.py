from flask import Flask, render_template, jsonify, request
from scripts import popularmovies, recomendar, getMovieList, getByWatchlist

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/watchlist/<username>')
def watchlist(username):
    movielist = getMovieList(getByWatchlist(username))
    if movielist:
        return render_template("watchlist.html", movielist=movielist, username=username)
    return jsonify({"error": "Request body must be JSON"}), 400

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json() 
    if not data or 'movielist' not in data:
        return jsonify({"mensagem": "Request movielist is empty"}), 400
    filme = recomendar(data['movielist'])
    return jsonify(filme)
    
    
if __name__ == "__main__":
    app.run()