from custom_exceptions.duplicate_jersey_number_exception import DuplicateJerseyNumberException
from data_access_layer.implementation_classes.player_postgres_dao import PlayerPostgresDAO
from entities.players import Player
from service_layer.abstract_services.player_service import PlayerService


class PlayerPostgresService(PlayerService):
    def __init__(self, player_dao: PlayerPostgresDAO):
        self.player_dao = player_dao

    # need to check and make sure players do not have the same jersey number
    def service_create_player_entry(self, player: Player) -> Player:
        players = self.player_dao.get_all_players_information()
        for existing_player in players:
            if existing_player.team_id == player.team_id:
                if existing_player.jersey_number == player.jersey_number:
                    raise DuplicateJerseyNumberException("Jersey number is already taken!")
        created_player = self.player_dao.create_player_entry(player)
        return created_player

    def service_get_player_information(self, player_id: int) -> Player:
        return self.player_dao.get_player_information(player_id)

    def service_get_all_players_information(self) -> list[Player]:
        return self.player_dao.get_all_players_information()

    # need to check and make sure players do not have the same jersey number
    def service_update_player_information(self, player: Player) -> Player:
        players = self.player_dao.get_all_players_information()
        for current_player in players:
            if current_player.team_id == player.team_id:
                if current_player.player_id != player.player_id:
                    if current_player.jersey_number == player.jersey_number:
                        raise DuplicateJerseyNumberException("Jersey number is already taken!")
        updated_player = self.player_dao.update_player_information(player)
        return updated_player

    def service_delete_player_information(self, player_id: int) -> bool:
        return self.player_dao.delete_player_information(player_id)