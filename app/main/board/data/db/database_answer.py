import sqlite3
from sqlite3 import OperationalError

from app.general.database import DataBase
from app.main.board.data.models.Answer import Answer


class DatabaseAnswer:

    path = DataBase.base_path + '/dbs/database'

    @staticmethod
    def create_db():
        try:
            sql = "CREATE TABLE ANSWER(" \
                  "ANSWER_ID INTEGER PRIMARY KEY AUTOINCREMENT," \
                  "CATEGORY_ID INTEGER NOT NULL," \
                  "PLAYER_ID INTEGER NOT NULL," \
                  "TEXT TEXT NOT NULL" \
                  ")"
            DataBase.make_no_response_query(sql, DatabaseAnswer.path)
        except OperationalError:
            print("TABLE ANSWER EXISTS")

    @staticmethod
    def drop_db():
        try:
            sql = "DROP TABLE ANSWER"
            DataBase.make_no_response_query(sql, DatabaseAnswer.path)
        except OperationalError:
            print("Table ANSWER dont Exists")

    @staticmethod
    def get_answers_from_category_by_category_id(category_id):
        query = "SELECT * FROM ANSWER WHERE CATEGORY_ID = {}".format(category_id)
        answers = []
        answer = DataBase.make_multi_response_query(query, DatabaseAnswer.path)
        for cat in answer:
            if cat:
                answers.append(Answer(int(cat[0]), int(cat[1]), int(cat[2]), cat[3]))
        return answers

    @staticmethod
    def get_by_answer_id(answer_id):
        query = "SELECT * FROM ANSWER WHERE ANSWER_ID = {}".format(answer_id)
        answer = DataBase.make_multi_response_query(query, DatabaseAnswer.path)
        if answer and len(answer) == 1:
            player_obj = answer[0]
            if player_obj:
                answer = Answer(int(player_obj[0]), int(player_obj[1]), int(player_obj[2]), player_obj[3])
                return answer
            else:
                return player_obj
        else:
            AttributeError()

    @staticmethod
    def insert_answer(category_id, player_id, text):
        connection = sqlite3.connect(DatabaseAnswer.path)
        cursor = connection.cursor()
        query = "INSERT INTO ANSWER(CATEGORY_ID, PLAYER_ID, TEXT) " \
                "VALUES({}, {}, '{}')".format(category_id, player_id, text)
        cursor.execute(query)
        answer_id = cursor.lastrowid
        connection.commit()
        connection.close()

        return DatabaseAnswer.get_by_answer_id(answer_id)
