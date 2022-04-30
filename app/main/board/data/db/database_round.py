import sqlite3
from sqlite3 import OperationalError

from app.general.database import DataBase
from app.main.board.data.models.Answer import Answer
from app.main.board.data.models.Round import Round


class DatabaseRound:

    path = DataBase.base_path + '/dbs/database'

    @staticmethod
    def create_db():
        try:
            sql = "CREATE TABLE ROUND(" \
                  "ROUND_ID INTEGER PRIMARY KEY AUTOINCREMENT," \
                  "GAME_ID INTEGER NOT NULL," \
                  "LETTER TEXT NOT NULL" \
                  ")"
            DataBase.make_no_response_query(sql, DatabaseRound.path)
        except OperationalError:
            print("TABLE ROUND EXISTS")

    @staticmethod
    def drop_db():
        try:
            sql = "DROP TABLE ROUND"
            DataBase.make_no_response_query(sql, DatabaseRound.path)
        except OperationalError:
            print("Table ROUND dont Exists")

    @staticmethod
    def get_rounds_from_game_by_game_id(game_id):
        query = "SELECT * FROM ROUND WHERE GAME_ID = {}".format(game_id)
        rounds = []
        anwser = DataBase.make_multi_response_query(query, DatabaseRound.path)
        for cat in anwser:
            if cat:
                rounds.append(Round(int(cat[0]), int(cat[1]), cat[2]))
        return rounds

    @staticmethod
    def get_by_round_id(round_id):
        query = "SELECT * FROM ROUND WHERE ROUND_ID = {}".format(round_id)
        anwser = DataBase.make_multi_response_query(query, DatabaseRound.path)
        if anwser and len(anwser) == 1:
            player_obj = anwser[0]
            if player_obj:
                round = Round(int(player_obj[0]), int(player_obj[1]), player_obj[2])
                return round
            else:
                return player_obj
        else:
            AttributeError()

    @staticmethod
    def insert_round(game_id, letter):
        connection = sqlite3.connect(DatabaseRound.path)
        cursor = connection.cursor()
        query = "INSERT INTO ROUND(GAME_ID, LETTER) " \
                "VALUES({}, '{}')".format(game_id, letter)
        cursor.execute(query)
        round_id = cursor.lastrowid
        connection.commit()
        connection.close()

        return DatabaseRound.get_by_round_id(round_id)

