from custom_exceptions.duplicate_team_name_exception import DuplicateTeamNameException
from data_access_layer.implementation_classes.team_dao_imp import TeamDAOImp
from entities.teams import Team
from service_layer.implementation_services.team_service_imp import TeamServiceImp

team_dao = TeamDAOImp()
team_service = TeamServiceImp(team_dao)

bad_team = Team(0, "duplicate name")
bad_update_team = Team(1, "duplicate name")


def test_catch_creating_team_with_duplicate_name():
    try:
        team_service.service_create_team(bad_team)
        assert False
    except DuplicateTeamNameException as e:
        assert str(e) == "You can not use that name: it is already taken"


def test_catch_updating_team_with_duplicate_name():
    try:
        team_service.service_update_team_information(bad_update_team)
        assert False
    except DuplicateTeamNameException as e:
        assert str(e) == "You can not use that name: it is already taken"
