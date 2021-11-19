from abc import ABC, abstractmethod

from entities.players import Player


class PlayerService(ABC):

    # create player method
    @abstractmethod
    def service_create_player_entry(self, player: Player) -> Player:
        pass

    # get player information
    @abstractmethod
    def service_get_player_information(self, player_id: int) -> Player:
        pass

    # get all player information
    @abstractmethod
    def service_get_all_players_information(self) -> list[Player]:
        pass

    # update player information
    @abstractmethod
    def service_update_player_information(self, player: Player) -> Player:
        pass

    # delete player information
    @abstractmethod
    def service_delete_player_information(self, player_id: int) -> bool:
        pass