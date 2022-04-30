class Game:
    game_id = 0

    def __init__(self, game_id):
        self.game_id = game_id

    def __repr__(self):
        return str({"game_id": self.game_id}).replace("'", "\"")
