from flask import Flask, render_template, jsonify, request, url_for
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from scripts import getMovie, getMovieList, getByWatchlist, getUrl

app = Flask(__name__)

limiter = Limiter(
    key_func = get_remote_address,
    app=app,
    default_limits=["200 per day", "30 per hour"],
)
@app.route("/favicon.ico")
def favicon():
    return app.send_static_file("favicon.ico")

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
    filme,remaining = getMovie(data['movielist'])
    return jsonify({"filme": filme, "remaining": remaining}), 200
    
@app.route('/random')
@limiter.limit("5 per minute")
def random():
    movieList = getMovieList(getUrl())
    if movieList:
        return render_template("random.html", movielist=movieList)
    return jsonify({"error": "erro in get list"}), 400

@app.errorhandler(429)
def ratelimit_handler(e):
    return jsonify({"error": "Too many requests, please try again later."}), 429

if __name__ == "__main__":
    app.run()