from datetime import timedelta, datetime
import random
import sqlite3
import string
from sqlite3 import OperationalError

from app.main.player.data.models.Player import Player
from app.general.database import DataBase


class DatabasePlayer:

    path = DataBase.base_path + '/dbs/database'

    @staticmethod
    def create_db():
        try:
            sql = "CREATE TABLE PLAYER(" \
                    "PLAYER_ID INTEGER PRIMARY KEY AUTOINCREMENT," \
                    "USERNAME TEXT UNIQUE NOT NULL, " \
                    "PASSWORD TEXT NOT NULL" \
                  ")"
            DataBase.make_no_response_query(sql, DatabasePlayer.path)
        except OperationalError:
            print("Table data Exists")

    @staticmethod
    def drop_db():
        try:
            sql = "DROP TABLE PLAYER"
            DataBase.make_no_response_query(sql, DatabasePlayer.path)
        except OperationalError:
            print("Table data dont Exists")

    @staticmethod
    def get_all_player():
        query = "SELECT * FROM PLAYER"
        players = []
        answers = DataBase.make_multi_response_query(query, DatabasePlayer.path)
        for player in answers:
            if player:
                players.append(Player(int(player[0]), player[1], player[2]))
        return players

    @staticmethod
    def get_by_player_name(player_name):
        query = "SELECT * FROM PLAYER WHERE USERNAME = '{}'".format(player_name)
        answer = DataBase.make_multi_response_query(query, DatabasePlayer.path)
        if answer and len(answer) == 1:
            player_obj = answer[0]
            if player_obj:
                player = Player(int(player_obj[0]), player_obj[1], player_obj[2])
                return player
            else:
                return player_obj
        else:
            AttributeError()

    @staticmethod
    def delete_player_by_player_id(player_id):
        response = DatabasePlayer.get_by_player_id(player_id)
        query = "DELETE FROM PLAYER WHERE PLAYER_ID = {}".format(player_id)
        DataBase.make_no_response_query(query, DatabasePlayer.path)
        return response

    @staticmethod
    def update_player_by_player_id(player_id, playername, password):
        query = "UPDATE PLAYER SET USERNAME = '{}', PASSWORD = '{}' WHERE PLAYER_ID = {}".format(playername, password, player_id)
        DataBase.make_no_response_query(query, DatabasePlayer.path)
        return str(DatabasePlayer.get_by_player_id(player_id))

    @staticmethod
    def get_by_player_id(player_id):
        query = "SELECT * FROM PLAYER WHERE PLAYER_ID = {}".format(player_id)
        answer = DataBase.make_multi_response_query(query, DatabasePlayer.path)
        if len(answer) == 1:
            player_obj = answer[0]
            if player_obj:
                player = Player(int(player_obj[0]), player_obj[1], player_obj[2])
                return player
            else:
                return player_obj
        else:
            AttributeError()

    @staticmethod
    def check_pw(player_id, pw):
        try:
            if DatabasePlayer.get_by_player_id(player_id).password == pw:
                return True
            else:
                return False
        except AttributeError:
            return False

    @staticmethod
    def insert_player(playername, pw):
        connection = sqlite3.connect(DatabasePlayer.path)
        cursor = connection.cursor()
        query = "INSERT INTO PLAYER(USERNAME, PASSWORD) VALUES('{}','{}')".format(playername, pw)
        cursor.execute(query)
        player_id = cursor.lastrowid
        connection.commit()
        connection.close()
        return DatabasePlayer.get_by_player_id(player_id)



