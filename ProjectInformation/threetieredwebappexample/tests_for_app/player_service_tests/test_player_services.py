from custom_exceptions.duplicate_jersey_number_exception import DuplicateJerseyNumberException
from data_access_layer.implementation_classes.player_dao_imp import PlayerDAOImp
from entities.players import Player
from service_layer.implementation_services.player_service_imp import PlayerServiceImp

player_dao = PlayerDAOImp()
player_service = PlayerServiceImp(player_dao)
player = Player("service", "testing", 100, 0, 1)
player_update = Player("update", "test", 100, 2, 1)


def test_validate_create_player_method():
    try:
        for existing_player in player_service.player_dao.player_list:
            print(existing_player)
        unexpected_player = player_service.service_create_player_entry(player)
        print()
        for existing_player in player_service.player_dao.player_list:
            print(existing_player)
            print()
        print(unexpected_player.player_id)
        assert False
    except DuplicateJerseyNumberException as e:
        assert str(e) == "Jersey number is already taken!"


def test_validate_update_player_method():
    try:
        player_service.service_update_player_information(player_update)
        assert False
    except DuplicateJerseyNumberException as e:
        assert str(e) == "Jersey number is already taken!"
