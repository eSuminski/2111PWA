from typing import List

from custom_exceptions.duplicate_team_name_exception import DuplicateTeamNameException
from data_access_layer.implementation_classes.team_postgres_dao import TeamPostgresDAO
from entities.teams import Team
from service_layer.abstract_services.team_service import TeamService


class TeamPostgresService(TeamService):
    def __init__(self, team_dao: TeamPostgresDAO):
        self.team_dao = team_dao

    # teams should not have the same name
    def service_create_team(self, team: Team) -> Team:
        teams_list = self.team_dao.get_all_teams()
        for t in teams_list:
            if t.name == team.name:
                raise DuplicateTeamNameException("That team name is already being used!")
        return self.team_dao.create_team(team)

    def service_get_team_by_id(self, team_id: int) -> Team:
        return self.team_dao.get_team_by_id(team_id)

    def service_get_all_teams(self) -> List[Team]:
        return self.team_dao.get_all_teams()

    # teams should not have the same name
    def service_update_team_information(self, team: Team) -> Team:
        teams_list = self.team_dao.get_all_teams()
        for t in teams_list:
            if t.name == team.name:
                raise DuplicateTeamNameException("That team name is already being used!")
        return self.team_dao.update_team_information(team)

    def service_delete_team_information(self, team_id: int) -> bool:
        return self.team_dao.delete_team_information(team_id)
