from custom_exceptions.duplicate_team_name_exception import DuplicateTeamNameException
from data_access_layer.implementation_classes.team_postgres_dao import TeamPostgresDAO
from entities.teams import Team
from service_layer.implementation_services.team_postgres_service import TeamPostgresService

team_dao = TeamPostgresDAO()
team_service = TeamPostgresService(team_dao)

bad_team = Team(1, "Portland Trail Blazers")


def test_catch_duplicate_name_create():
    try:
        team_service.service_create_team(bad_team)
        assert False
    except DuplicateTeamNameException as e:
        assert str(e) == "That team name is already being used!"


def test_catch_duplicate_name_update():
    try:
        team_service.service_update_team_information(bad_team)
        assert False
    except DuplicateTeamNameException as e:
        assert str(e) == "That team name is already being used!"
