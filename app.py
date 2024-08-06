from typing import Text
from flask import Flask, jsonify, render_template, request, redirect, url_for
from database import WORKS

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html', works=WORKS)


@app.route('/api/works')
def art_list():
    return jsonify(WORKS)


@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
