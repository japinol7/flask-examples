import requests
from flask import render_template, request
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Flask 02 Example. Calling APIs')


@app.route('/pokemon', methods=['GET', 'POST'])
def pokemon():
    pokemon = []
    if request.method == 'POST' and 'pokemon_color' in request.form:
        colour = request.form.get('pokemon_color')
        pokemon = get_pokemon_of_colour(colour)
    return render_template('pokemon.html', pokemon=pokemon)


@app.route('/about')
def about():
    return render_template('about.html')


def get_pokemon_of_colour(colour):
    r = requests.get('https://pokeapi.co/api/v2/pokemon-color/' + colour.lower())
    if not r.ok:
        return colour, 0, []

    pokemon = []
    pokedata = r.json()
    for item in pokedata['pokemon_species']:
        pokemon.append((item['name'], item['url']))

    return colour, len(pokemon), pokemon
