class Player:
    def __init__(self, first_name: str, last_name: str, jersey_number: int, player_id: int):
        self.first_name = first_name
        self.last_name = last_name
        self.jersey_number = jersey_number
        self.player_id = player_id

    def make_player_dictionary(self):
        return {
            "firstName": self.first_name,
            "lastName": self.last_name,
            "jerseyNumber": self.jersey_number,
            "playerId": self.player_id
        }




