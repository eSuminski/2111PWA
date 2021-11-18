from data_access_layer.implementation_classes.player_dao_imp import PlayerDAOImp
from entities.players import Player

player_dao_imp = PlayerDAOImp()
player = Player("Test", "Player", 12, 0)


def test_create_player_success():
    new_player: Player = player_dao_imp.create_player_entry(player)
    assert new_player.player_id != 0


def test_get_player_success():
    pass


def test_get_all_players_success():
    pass


def test_update_player_success():
    pass


def test_delete_player_success():
    pass
