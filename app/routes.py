import datetime
import json
import sqlite3

from flask import request, abort
from password_strength import PasswordPolicy

from app.main.board.data.db.database_answer import DatabaseAnswer
from app.main.board.data.db.database_game import DatabaseGame
from app.main.board.data.db.database_round import DatabaseRound
from app.main.player.data.db.database_player import DatabasePlayer
from app.main.board.data.db.database_category import DatabaseCategory
from app import app

policy = PasswordPolicy.from_names(
    length=8,
    uppercase=1,
    numbers=1
)


DatabasePlayer.create_db()
DatabaseCategory.create_db()
DatabaseAnswer.create_db()
DatabaseGame.create_db()
DatabaseRound.create_db()


@app.route('/player', methods=['GET'])
def get_categorys():
    try:
        player = DatabasePlayer.get_all_player()
        return str(player)
    except AttributeError:
        abort(404)


@app.route('/player/<player_id>', methods=['GET'])
def get_player_by_player_is(player_id):
    try:
        player = DatabasePlayer.get_by_player_id(player_id)
        if player:
            return str(player)
        else:
            abort(404)
    except AttributeError:
        abort(404)


@app.route('/player', methods=['POST'])
def insert_player():
    data = request.get_json(force=True)
    username = data["username"]
    pw = data["password"]
    try:
        player = DatabasePlayer.insert_player(username, pw)
        if player:
            return str(player)
        else:
            abort(404)
    except AttributeError:
        abort(404)


@app.route('/categorys', methods=['GET'])
def get_categorys():
    try:
        categorys = DatabaseCategory.get_categorys()
        return str(categorys)
    except AttributeError:
        abort(404)


@app.route('/category', methods=['POST'])
def insert_category():
    data = request.get_json(force=True)
    name = data["name"]
    proposal = data["proposal"]
    game_id = data["game_id"]
    try:
        category = DatabaseCategory.insert_category(game_id, name, proposal)
        return str(category)
    except AttributeError:
        abort(404)


@app.route('/category/<cat_id>', methods=['GET'])
def get_category_by_cat_id(cat_id):
    try:
        category = DatabaseCategory.get_by_category_id(cat_id)
        if category:
            return str(category)
        else:
            abort(404)
    except AttributeError:
        abort(404)


@app.route('/game', methods=['POST'])
def insert_game():
    try:
        category = DatabaseGame.insert_game()
        return str(category)
    except AttributeError:
        abort(404)


@app.route('/games', methods=['GET'])
def get_all_games():
    try:
        category = DatabaseGame.get_all_games()
        return str(category)
    except AttributeError:
        abort(404)


@app.route('/game/<game_id>', methods=['GET'])
def get_game(game_id):
    try:
        category = DatabaseGame.get_by_game_id(game_id)
        return str(category)
    except AttributeError:
        abort(404)


@app.route('/game/<game_id>/categorys', methods=['GET'])
def get_gategorys_of_game(game_id):
    try:
        category = DatabaseCategory.get_categorys_by_game_by_game_id(game_id)
        return str(category)
    except AttributeError:
        abort(404)


@app.route('/round', methods=['POST'])
def insert_round():
    data = request.get_json(force=True)
    game_id = data["game_id"]
    letter = data["letter"]
    try:
        round = DatabaseRound.insert_round(game_id, letter)
        return str(round)
    except AttributeError:
        abort(404)


@app.route('/round/<round_id>', methods=['GET'])
def get_all_rounds(round_id):
    try:
        category = DatabaseRound.get_by_round_id(round_id)
        return str(category)
    except AttributeError:
        abort(404)


@app.route('/game/<game_id>/rounds', methods=['GET'])
def get_all_rounds_of_game(game_id):
    try:
        category = DatabaseRound.get_rounds_from_game_by_game_id(game_id)
        return str(category)
    except AttributeError:
        abort(404)


@app.route('/answer', methods=['POST'])
def insert_answer():
    data = request.get_json(force=True)
    cat_id = data["cat_id"]
    player_id = data["player_id"]
    text = data["text"]
    try:
        category = DatabaseAnswer.insert_answer(cat_id, player_id, text)
        return str(category)
    except AttributeError:
        abort(404)


@app.route('/category/<cat_id>/answers', methods=['GET'])
def get_all_answers_of_cat(cat_id):
    try:
        category = DatabaseAnswer.get_answers_from_category_by_category_id(cat_id)
        return str(category)
    except AttributeError:
        abort(404)
