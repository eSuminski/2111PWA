from data_access_layer.abstract_classes.login_dao import LoginDAO
from util.database_connection import connection


class LoginPostgresDAO(LoginDAO):

    def get_login_by_credentials(self, username: str, password: str):
        sql = "select login_id from login where username = %s and password = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (username, password))
        validated = cursor.fetchone()
        return validated
