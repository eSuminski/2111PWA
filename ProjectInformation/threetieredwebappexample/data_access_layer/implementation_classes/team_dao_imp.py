from typing import List

from data_access_layer.abstract_classes.team_dao import TeamDAO
from entities.teams import Team


class TeamDAOImp(TeamDAO):

    # NEED TO ADD PREMADE DATA FOR TESTS WHEN THEY ARE CREATED
    team_one = Team(1,"first team")
    team_two = Team(2, "second team")
    team_three = Team(3, "to be deleted")
    team_four = Team(4, "duplicate name")
    team_list = [team_one, team_two, team_three, team_four]
    team_id_generator = 5

    def create_team(self, team: Team) -> Team:
        new_team = team
        new_team.team_id = TeamDAOImp.team_id_generator
        TeamDAOImp.team_id_generator += 1
        TeamDAOImp.team_list.append(new_team)
        return new_team

    def get_team_by_id(self, team_id: int) -> Team:
        for team in TeamDAOImp.team_list:
            if team.team_id == team_id:
                return team

    def get_all_teams(self) -> List[Team]:
        return TeamDAOImp.team_list

    def update_team_information(self, team: Team) -> Team:
        for team_in_list in TeamDAOImp.team_list:
            if team_in_list.team_id == team.team_id:
                team_in_list.name = team.name
                return team_in_list

    def delete_team_information(self, team_id: int) -> bool:
        for team in TeamDAOImp.team_list:
            if team.team_id == team_id:
                index = TeamDAOImp.team_list.index(team)
                del TeamDAOImp.team_list[index]
                return True