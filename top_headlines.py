from flask import Flask, render_template, request
from secrets1 import *
import requests

app = Flask(__name__)

@app.route('/')
def welcome():
    return '<h1> Welcome!</h1>'


@app.route('/name/<name>')
def name(name):
    return render_template('name.html', name=name)

@app.route('/headlines/<name>')
def read_artical(name):
    base_url = 'https://api.nytimes.com/svc/topstories/v2/technology.json?api-key=' + api_key
    results = requests.get(base_url).json()
    results = results['results']
    headlines = [ele['title'] for ele in results[:5]]
    return render_template('read_artical.html', name=name, headlines=headlines)


if __name__ == '__main__':

    print('starting Flask app', app.name)

    app.run(debug=True)
