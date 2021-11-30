from data_access_layer.implementation_classes.player_postgres_dao import PlayerPostgresDAO
from entities.players import Player

player_dao = PlayerPostgresDAO()
player: Player = Player("first", "last", 23, 0, 1)

random_names = {"Bob"}
random_names.add("Sally")
random_names.add("Bill")
random_names.add("Susie")

random_name = random_names.pop()

update_player = Player(random_name, "player", 200, 12, 1)

player_to_delete = Player(random_names.pop(), random_names.pop(), 0, 0, 1)


def test_create_player_success():
    created_player = player_dao.create_player_entry(player)
    assert created_player.player_id != 0


def test_get_player_success():
    brandon_roy = player_dao.get_player_information(1)
    assert brandon_roy.first_name == "Brandon" and brandon_roy.last_name == "Roy"


def test_get_all_players_success():
    players = player_dao.get_all_players_information()
    assert len(players) > 2


def test_update_player_success():
    updated_player = player_dao.update_player_information(update_player)
    assert updated_player.first_name == random_name


def test_delete_player_success():
    player_to_be_deleted = player_dao.create_player_entry(player_to_delete)
    result = player_dao.delete_player_information(player_to_be_deleted.player_id)
    assert result
