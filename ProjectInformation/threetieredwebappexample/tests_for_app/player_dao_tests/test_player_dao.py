from data_access_layer.implementation_classes.player_dao_imp import PlayerDAOImp
from data_access_layer.implementation_classes.player_postgres_dao import PlayerPostgresDAO
from entities.players import Player

player_dao_imp = PlayerDAOImp()
player = Player("Test", "Player", 12, 0, 1)


def test_create_player_success():
    new_player = player_dao_imp.create_player_entry(player)
    for players in player_dao_imp.player_list:
        print(players)
    print(new_player.player_id)
    assert new_player.player_id != 0


def test_get_player_success():
    returned_player: Player = player_dao_imp.get_player_information(1)
    assert returned_player.player_id == 1


def test_get_all_players_success():
    player_list = player_dao_imp.get_all_players_information()
    assert len(player_list) >= 2


def test_update_player_success():
    updated_info = Player("changed by", "update player method", 105, 1, 1)
    updated_player: Player = player_dao_imp.update_player_information(updated_info)
    assert updated_player.jersey_number == updated_info.jersey_number


def test_delete_player_success():
    confirm_player_deleted = player_dao_imp.delete_player_information(3)
    assert confirm_player_deleted
