class Category:
    cat_id = 0
    name = ""
    proposal = ""

    def __init__(self, cat_id, name, proposal):
        self.cat_id = cat_id
        self.name = name
        self.proposal = proposal

    def __repr__(self):
        return str({"cat_id": self.cat_id, "name": self.name, "proposal": self.proposal}).replace("'", "\"")
