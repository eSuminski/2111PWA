from data_access_layer.abstract_classes.player_dao import PlayerDAO
from entities.players import Player


class PlayerDAOImp(PlayerDAO):
    player_list = []
    player_id_generator = 0

    def create_player_entry(self, player: Player):
        pass

    def get_player_information(self, player_id: int):
        pass

    def get_all_players_information(self):
        pass

    def update_player_information(self, player: Player):
        pass

    def delete_player_information(self, player_id: int):
        pass
