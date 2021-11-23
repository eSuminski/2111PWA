from data_access_layer.abstract_classes.player_dao import PlayerDAO
from entities.players import Player


class PlayerDAOImp(PlayerDAO):
    # these players are premade so that we can test our methods
    premade_player = Player("Premade", "Player", 100, 1, 1)
    premade_player_two = Player("added for", "get all player test", 101, 2, 1)
    to_delete = Player("I exist", "to be deleted", 0, 3, 1)

    # we are going to use this list as our "database"
    player_list = [premade_player, premade_player_two, to_delete]
    # we are going to use this value to assign unique player ids
    player_id_generator = 4

    def create_player_entry(self, player: Player) -> Player:
        player.player_id = PlayerDAOImp.player_id_generator
        PlayerDAOImp.player_id_generator += 1
        PlayerDAOImp.player_list.append(player)
        return player

    def get_player_information(self, player_id: int) -> Player:
        for player in PlayerDAOImp.player_list:
            if player.player_id == player_id:
                return player

    def get_all_players_information(self) -> list[Player]:
        return PlayerDAOImp.player_list

    def update_player_information(self, player: Player) -> Player:
        for player_in_list in PlayerDAOImp.player_list:
            if player_in_list.player_id == player.player_id:
                index = PlayerDAOImp.player_list.index(player_in_list)
                PlayerDAOImp.player_list[index] = player
                return player

    def delete_player_information(self, player_id: int) -> bool:
        for player_in_list in PlayerDAOImp.player_list:
            if player_in_list.player_id == player_id:
                index = PlayerDAOImp.player_list.index(player_in_list)
                del PlayerDAOImp.player_list[index]
                return True
