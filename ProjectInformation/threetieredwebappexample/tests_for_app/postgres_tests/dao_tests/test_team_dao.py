from data_access_layer.implementation_classes.team_postgres_dao import TeamPostgresDAO
from entities.teams import Team

team_dao = TeamPostgresDAO()

new_team = Team(0, "test team")
team_names = {'Lakers'}
team_names.add('Celtics')
team_names.add('Rockets')
team_names.add('Blazers')
new_name = team_names.pop()
update_team = Team(3, new_name)

deleted_name = team_names.pop()
delete_team = Team(0, deleted_name)


def test_create_team_success():
    team_result = team_dao.create_team(new_team)
    assert team_result.team_id != 0


def test_select_team_by_id_success():
    initial_team = team_dao.get_team_by_id(1)
    assert initial_team.team_id == 1


def test_select_all_teams_success():
    teams = team_dao.get_all_teams()
    assert len(teams) >= 3


def test_update_team_success():
    updated_team = team_dao.update_team_information(update_team)
    assert updated_team.name == new_name


def test_delete_team_success():
    to_be_deleted = team_dao.create_team(delete_team)
    result = team_dao.delete_team_information(to_be_deleted.team_id)
    assert result
