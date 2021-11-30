from typing import List

from data_access_layer.abstract_classes.team_dao import TeamDAO
from entities.teams import Team
from util.database_connection import connection


class TeamPostgresDAO(TeamDAO):
    def create_team(self, team: Team) -> Team:
        sql = "insert into team values(default, %s) returning team_id"
        cursor = connection.cursor()
        cursor.execute(sql, [team.team_id])
        connection.commit()
        generated_id = cursor.fetchone()[0]
        team.team_id = generated_id
        return team

    def get_team_by_id(self, team_id: int) -> Team:
        sql = "select * from team where team_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [team_id])
        team_record = cursor.fetchone()
        team = Team(*team_record)
        return team

    def get_all_teams(self) -> List[Team]:
        sql = "select * from team"
        cursor = connection.cursor()
        cursor.execute(sql)
        team_records = cursor.fetchall()
        teams = []
        for team in team_records:
            teams.append(Team(*team))
        return teams

    def update_team_information(self, team: Team) -> Team:
        sql = "update team set name = %s where team_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (team.name, team.team_id))
        connection.commit()
        return team

    def delete_team_information(self, team_id: int) -> bool:
        sql = "delete from team where team_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [team_id])
        connection.commit()
        return True
