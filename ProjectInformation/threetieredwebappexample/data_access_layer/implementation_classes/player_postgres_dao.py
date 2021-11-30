from data_access_layer.abstract_classes.player_dao import PlayerDAO
from util.database_connection import connection
from entities.players import Player


class PlayerPostgresDAO(PlayerDAO):
    def create_player_entry(self, player: Player) -> Player:
        # we will use %s as placeholders for our values
        sql = "insert into player values(%s, %s, %s, default, %s) returning player_id"
        cursor = connection.cursor()
        # we pass in our sql to the cursor's execute method, and inside a tuple we then pass in the
        # values for the insert command
        cursor.execute(sql, (player.first_name, player.last_name, player.jersey_number, player.team_id))
        connection.commit()
        player_id = cursor.fetchone()[0]
        player.player_id = player_id
        return player

    def get_player_information(self, player_id: int) -> Player:
        sql = "select * from player where player_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [player_id])
        player_record = cursor.fetchone()
        player = Player(*player_record)
        return player

    def get_all_players_information(self) -> list[Player]:
        sql = "select * from player"
        cursor = connection.cursor()
        cursor.execute(sql)
        player_records = cursor.fetchall()
        player_list = []
        for player in player_records:
            player_list.append(Player(*player))
        return player_list

    def update_player_information(self, player: Player) -> Player:
        sql = "update player set first_name = %s, last_name = %s, jersey_number = %s, team_id = %s where player_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (player.first_name, player.last_name, player.jersey_number, player.team_id, player.player_id))
        connection.commit()
        return player

    def delete_player_information(self, player_id: int) -> bool:
        sql = "delete from player where player_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [player_id])
        connection.commit()
        return True
