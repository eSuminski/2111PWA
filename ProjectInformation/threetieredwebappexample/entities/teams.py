class Team:
    def __init__(self, team_id: int, name: str):
        self.team_id = team_id
        self.name = name

    def __str__(self):
        return "Id: {}, name: {}".format(self.team_id, self.name)

    def create_team_dictionary(self):
        return {
            "teamId": self.team_id,
            "name": self.name
        }
