from flask import Flask
from flask import jsonify
from flask import session
from flask import url_for, redirect, request
from app.game import Game
from app.game import Grid
import json

app = Flask(__name__, static_folder='static')


@app.route("/")
def index():
    return redirect(url_for('static', filename='index.html'))


@app.route("/start", methods=['POST'])
def start():
    input = bytes.decode(request.data)
    inputDict = json.loads(input)
    x, y = int(inputDict['x']), int(inputDict['y'])
    g = Game(x, y)
    level = g.grid.serialize_level()
    session['level'] = level
    return jsonify(level=session['level'], endgame=False, size=[g.grid.height, g.grid.width])


@app.route("/move", methods=['POST'])
def move():
    input = bytes.decode(request.data)
    inputDict = json.loads(input)
    x, y = inputDict['x'], inputDict['y']

    imported_level = session['level']
    level = Grid.import_level(imported_level)

    imported_game = Game(len(level), len(level[0]))
    imported_game.grid.level = level
    cell = imported_game.grid.get_cell(x, y)

    imported_game.rules.move(cell, imported_game.grid)

    export_level = imported_game.grid.serialize_level()

    session['level'] = export_level
    gamestatus = imported_game.rules.is_game_over(imported_game.grid)
    return jsonify(level=session['level'], endgame=gamestatus)


if __name__ == "__main__":
    #app session secret key, change it to use
    key = ""
    #test_key = "\xcc\xeb\x1f\xe2\x91\xb9co\\\xe0\xf8\xccD\xa0\xe8u\x7f6\xfb'\xdd\x97\x10A"
    if(not key):
        raise Exception("Generate a secret key before starting this demo")
    app.secret_key = key
    app.run()
