class Player:
    player_id = 0
    username = ""
    password = ""

    def __init__(self, player_id, username, password):
        self.player_id = player_id
        self.username = username
        self.password = password

    def __repr__(self):
        return str({"player_id": self.player_id, "username": self.username}).replace("'", "\"")


