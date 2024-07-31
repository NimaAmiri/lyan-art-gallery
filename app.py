from flask import Flask, jsonify, render_template, request, redirect, url_for
from os import path

app = Flask(__name__)

WORKS = [{
    'id': 1,
    'title': 'The Scream',
    'images_id': 'the_scream',
    'year': '1893',
    'description': 'A painting of a young woman screaming in fear.',
    'img_url': 'https://en.wikipedia.org/wiki/The_Scream',
    'artist': 'Edvard Munch',
    'preis': '€10.000'
}, {
    'id': 2,
    'title': 'The Starry Night',
    'images_id': 'the_starry_night',
    'year': '1889',
    'description':
    'A painting of the starry night, painted by Vincent van Gogh.',
    'img_url': 'https://en.wikipedia.org/wiki/The_Starry_Night',
    'artist': 'Vincent van Gogh',
    'preis': '€15.000'
}, {
    'id': 3,
    'title': 'The Persistence of Memory',
    'images_id': 'the_persistence_of_memory',
    'year': '1931',
    'description': 'A painting of a man struggling to remember his past.',
    'img_url': 'https://en.wikipedia.org/wiki/The_Persistence_of_Memory',
    'artist': 'Salvador Dali',
    'preis': '€20.000'
}, {
    'id': 4,
    'title': 'The Last Supper',
    'images_id': 'the_last_supper',
    'year': '1904',
    'description': 'A painting of a crowd of people holding a ceremony.',
    'img_url': 'https://en.wikipedia.org/wiki/Last_Supper',
    'artist': 'Leonardo da Vinci',
    'preis': '€25.000'
}]


@app.route('/')
def index():
    return render_template('home.html', works=WORKS)


@app.route('/api/ works')
def art_list():
    return jsonify(WORKS)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
