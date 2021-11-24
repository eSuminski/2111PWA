from abc import ABC, abstractmethod
from typing import List

from entities.teams import Team


class TeamService(ABC):

    # create team
    @abstractmethod
    def service_create_team(self, team: Team) -> Team:
        pass

    # get team
    @abstractmethod
    def service_get_team_by_id(self, team_id: int) -> Team:
        pass

    # get all teams
    @abstractmethod
    def service_get_all_teams(self) -> List[Team]:
        pass

    # update team
    @abstractmethod
    def service_update_team_information(self, team: Team) -> Team:
        pass

    # delete team
    @abstractmethod
    def service_delete_team_information(self, team_id: int) -> bool:
        pass
