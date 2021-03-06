from abc import ABC, abstractmethod

from entities.players import Player


class PlayerDAO(ABC):

    # create player method
    @abstractmethod
    def create_player_entry(self, player: Player) -> Player:
        pass

    # get player information
    @abstractmethod
    def get_player_information(self, player_id: int) -> Player:
        pass

    # get all player information
    @abstractmethod
    def get_all_players_information(self) -> list[Player]:
        pass

    # update player information
    @abstractmethod
    def update_player_information(self, player: Player) -> Player:
        pass

    # delete player information
    @abstractmethod
    def delete_player_information(self, player_id: int) -> bool:
        pass
