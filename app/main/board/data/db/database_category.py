import sqlite3
from sqlite3 import OperationalError

from app.general.database import DataBase
from app.main.board.data.models.Category import Category


class DatabaseCategory:

    path = DataBase.base_path + '/dbs/database'

    @staticmethod
    def create_db():
        try:
            sql = "CREATE TABLE CATEGORY(" \
                  "CATEGORY_ID INTEGER PRIMARY KEY AUTOINCREMENT," \
                  "GAME_ID INTEGER,"\
                  "USERNAME TEXT NOT NULL," \
                  "PROPOSAL TEXT" \
                  ")"
            DataBase.make_no_response_query(sql, DatabaseCategory.path)
        except OperationalError:
            print("TABLE CATEGORY EXISTS")

    @staticmethod
    def drop_db():
        try:
            sql = "DROP TABLE CATEGORY"
            DataBase.make_no_response_query(sql, DatabaseCategory.path)
        except OperationalError:
            print("Table CATEGORY dont Exists")

    @staticmethod
    def get_categorys():
        query = "SELECT * FROM CATEGORY"
        categorys = []
        answers = DataBase.make_multi_response_query(query, DatabaseCategory.path)
        for cat in answers:
            if cat:
                categorys.append(Category(int(cat[0]), cat[1], cat[2]))
        return categorys



    @staticmethod
    def get_by_category_id(category_id):
        query = "SELECT * FROM CATEGORY WHERE CATEGORY_ID = '{}'".format(category_id)
        answer = DataBase.make_multi_response_query(query, DatabaseCategory.path)
        if answer and len(answer) == 1:
            player_obj = answer[0]
            if player_obj:
                category = Category(int(player_obj[0]), int(player_obj[1]), player_obj[2], player_obj[3])
                return category
            else:
                return player_obj
        else:
            AttributeError()

    @staticmethod
    def get_categorys_by_game_by_game_id(game_id):
        query = "SELECT * FROM CATEGORY WHERE GAME_ID = '{}'".format(game_id)
        categorys = []
        answers = DataBase.make_multi_response_query(query, DatabaseCategory.path)
        for cat in answers:
            if cat:
                categorys.append(Category(int(cat[0]), int(cat[1]), cat[2], cat[3]))
        return categorys

    @staticmethod
    def insert_category(game_id, column_id, proposal):
        connection = sqlite3.connect(DatabaseCategory.path)
        cursor = connection.cursor()
        query = "INSERT INTO CATEGORY(GAME_ID, USERNAME, PROPOSAL) " \
                "VALUES({}, '{}', '{}')".format(game_id, column_id, proposal)
        cursor.execute(query)
        category_id = cursor.lastrowid
        connection.commit()
        connection.close()

        return DatabaseCategory.get_by_category_id(category_id)

