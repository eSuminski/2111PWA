from data_access_layer.implementation_classes.login_dao_postgres import LoginPostgresDAO

login_dao = LoginPostgresDAO()
username = "username"
password = "password"


def test_validate_login():
    validated = login_dao.get_login_by_credentials(username, password)
    assert validated[0] == 1


def test_not_valid_login():
    validated = login_dao.get_login_by_credentials("bad username", "bad password")
    assert validated is None
