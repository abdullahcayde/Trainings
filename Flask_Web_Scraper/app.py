from flask import Flask, render_template
import requests
import json


app = Flask(__name__)


@app.route('/')
def get_bee():
    r = requests.get('https://api.punkapi.com/v2/beers/random')
    beejson = r.json()
    print(beejson[0]['name'])
    print(beejson[0]['abv'])
    print(beejson[0]['description'])
    print(beejson[0]['food_pairing'][0])

    bee = {
        'name' : beejson[0]['name'],
        'abv' : beejson[0]['abv'],
        'desc' : beejson[0]['description'],
        'foodpair' : beejson[0]['food_pairing'][0]
    }

    print(bee)
    return render_template('index.html', title='Scrape', bee=bee)


if __name__ == '__main__':
    app.run(debug=True)


