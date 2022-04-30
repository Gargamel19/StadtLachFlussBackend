class Round:
    round_id = 0
    game_id = 0
    letter = ""

    def __init__(self, round_id, game_id, letter):
        self.round_id = round_id
        self.game_id = game_id
        self.letter = letter

    def __repr__(self):
        return str({"round_id": self.round_id, "game_id": self.game_id, "letter": self.letter}).replace("'", "\"")
