from typing import List

from custom_exceptions.duplicate_team_name_exception import DuplicateTeamNameException
from data_access_layer.implementation_classes.team_dao_imp import TeamDAOImp
from entities.teams import Team
from service_layer.abstract_services.team_service import TeamService


class TeamServiceImp(TeamService):
    # business logic: teams must not have the same name

    def __init__(self, team_dao: TeamDAOImp):
        self.team_dao = team_dao

    def service_create_team(self, team: Team) -> Team:
        for existing_team in self.team_dao.team_list:
            if existing_team.name == team.name:
                raise DuplicateTeamNameException("You can not use that name: it is already taken")
        new_team = self.team_dao.create_team(team)
        return new_team

    def service_get_team_by_id(self, team_id: int) -> Team:
        return self.team_dao.get_team_by_id(team_id)

    def service_get_all_teams(self) -> List[Team]:
        return self.team_dao.get_all_teams()

    def service_update_team_information(self, team: Team) -> Team:
        for existing_team in self.team_dao.team_list:
            if existing_team.team_id != team.team_id:
                if existing_team.name == team.name:
                    raise DuplicateTeamNameException("You can not use that name: it is already taken")
        updated_team = self.team_dao.update_team_information(team)
        return updated_team

    def service_delete_team_information(self, team_id: int) -> bool:
        return self.team_dao.delete_team_information(team_id)
