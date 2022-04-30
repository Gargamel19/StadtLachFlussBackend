class Answer:
    answer_id = 0
    category_id = 0
    player_id = 0
    text = ""

    def __init__(self, answer_id, category_id, player_id, text):
        self.answer_id = answer_id
        self.category_id = category_id
        self.player_id = player_id
        self.text = text

    def __repr__(self):
        return str({"answer_id": self.answer_id, "category_id": self.category_id, "player_id": self.player_id,
                    "text": self.text}).replace("'", "\"")