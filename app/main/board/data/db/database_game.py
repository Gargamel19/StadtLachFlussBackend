import sqlite3
from sqlite3 import OperationalError

from app.general.database import DataBase
from app.main.board.data.models.Answer import Answer
from app.main.board.data.models.Game import Game
from app.main.board.data.models.Round import Round


class DatabaseGame:

    path = DataBase.base_path + '/dbs/database'

    @staticmethod
    def create_db():
        try:
            sql = "CREATE TABLE GAME(" \
                  "GAME_ID INTEGER PRIMARY KEY AUTOINCREMENT" \
                  ")"
            DataBase.make_no_response_query(sql, DatabaseGame.path)
        except OperationalError:
            print("TABLE GAME EXISTS")

    @staticmethod
    def drop_db():
        try:
            sql = "DROP TABLE GAME"
            DataBase.make_no_response_query(sql, DatabaseGame.path)
        except OperationalError:
            print("Table GAME dont Exists")

    @staticmethod
    def get_by_game_id(game_id):
        query = "SELECT * FROM GAME WHERE GAME_ID = {}".format(game_id)
        anwser = DataBase.make_multi_response_query(query, DatabaseGame.path)
        if anwser and len(anwser) == 1:
            player_obj = anwser[0]
            if player_obj:
                game = Game(int(player_obj[0]))
                return game
            else:
                return player_obj
        else:
            AttributeError()

    @staticmethod
    def get_all_games():
        query = "SELECT * FROM GAME"
        answers = []
        answer = DataBase.make_multi_response_query(query, DatabaseGame.path)
        for cat in answer:
            if cat:
                answers.append(Game(int(cat[0])))
        return answers

    @staticmethod
    def insert_game():
        connection = sqlite3.connect(DatabaseGame.path)
        cursor = connection.cursor()
        query = "INSERT INTO GAME DEFAULT VALUES;"
        cursor.execute(query)
        game_id = cursor.lastrowid
        connection.commit()
        connection.close()

        return DatabaseGame.get_by_game_id(game_id)

