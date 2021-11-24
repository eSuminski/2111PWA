from data_access_layer.implementation_classes.team_dao_imp import TeamDAOImp
from entities.teams import Team

team_dao = TeamDAOImp()
test_team = Team(0, "test team")
updated_team = Team(2, "updated team")


def test_create_team_success():
    created_team = team_dao.create_team(test_team)
    assert created_team.team_id != 0


def test_select_team_by_id_success():
    selected_team = team_dao.get_team_by_id(1)
    assert selected_team.team_id == 1


def test_select_all_teams_success():
    teams = team_dao.get_all_teams()
    assert len(teams) >= 2


def test_update_team_success():
    result = team_dao.update_team_information(updated_team)
    assert result.name == "updated team"


def test_delete_team_success():
    result = team_dao.delete_team_information(3)
    assert result
