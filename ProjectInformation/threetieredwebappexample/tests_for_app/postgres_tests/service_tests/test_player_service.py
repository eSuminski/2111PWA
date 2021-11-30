from custom_exceptions.duplicate_jersey_number_exception import DuplicateJerseyNumberException
from data_access_layer.implementation_classes.player_postgres_dao import PlayerPostgresDAO
from entities.players import Player
from service_layer.implementation_services.player_postgres_service import PlayerPostgresService

player_dao = PlayerPostgresDAO()
player_service = PlayerPostgresService(player_dao)

player_with_duplicate_jersey = Player("first", "last", 200, 0, 1)


def test_catch_duplicate_jersey_number_for_create_method():
    try:
        player_service.service_create_player_entry(player_with_duplicate_jersey)
        assert False
    except DuplicateJerseyNumberException as e:
        assert str(e) == "Jersey number is already taken!"


def test_catch_duplicate_jersey_number_for_update_method():
    try:
        player_service.service_update_player_information(player_with_duplicate_jersey)
        assert False
    except DuplicateJerseyNumberException as e:
        assert str(e) == "Jersey number is already taken!"
