from custom_exceptions.duplicate_jersey_number_exception import DuplicateJerseyNumberException
from data_access_layer.implementation_classes.player_dao_imp import PlayerDAOImp
from entities.players import Player
from service_layer.abstract_services.player_service import PlayerService

"""
we are going to make use of dependency injection with our service class. This allows us to easily change the
implementation of our code by switching out the implementing class. Switching from a local to a cloud based database?
just pass in a cloud based implementation object into the service layer instead of a local based implementation object
"""


# BUSINESS LOGIC: players should have unique jersey numbers on the same team

class PlayerServiceImp(PlayerService):
    def __init__(self, player_dao):
        # we are doing dependency injection with this init dunder method
        self.player_dao: PlayerDAOImp = player_dao

    def service_create_player_entry(self, player: Player) -> Player:
        # need to implement business logic
        for current_player in self.player_dao.player_list:
            if current_player.team_id == player.team_id:
                if current_player.jersey_number == player.jersey_number:
                    raise DuplicateJerseyNumberException("Jersey number is already taken!")
        else:
            return self.player_dao.create_player_entry(player)

    def service_get_player_information(self, player_id: int) -> Player:
        return self.player_dao.get_player_information(player_id)

    def service_get_all_players_information(self) -> list[Player]:
        return self.player_dao.get_all_players_information()

    def service_update_player_information(self, player: Player) -> Player:
        for current_player in self.player_dao.player_list:
            if current_player.team_id == player.team_id:
                if current_player.jersey_number == player.jersey_number:
                    raise DuplicateJerseyNumberException("Jersey number is already taken!")
        else:
            return self.player_dao.update_player_information(player)

    def service_delete_player_information(self, player_id: int) -> bool:
        return self.player_dao.delete_player_information(player_id)
