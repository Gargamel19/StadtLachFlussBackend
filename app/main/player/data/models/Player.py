class Player:
    player_id = 0
    username = ""
    lifes = 5
    cam_url = ""

    def __init__(self, player_id, username, lifes, cam_url):
        self.player_id = player_id
        self.username = username
        self.lifes = lifes
        self.cam_url = cam_url

    def __repr__(self):
        return str({"player_id": self.player_id, "username": self.username, "lifes": self.lifes,
                    "cam_url": self.cam_url}).replace("'", "\"")