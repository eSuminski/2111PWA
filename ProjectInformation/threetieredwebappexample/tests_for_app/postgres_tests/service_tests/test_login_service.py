from data_access_layer.implementation_classes.login_dao_postgres import LoginPostgresDAO
from service_layer.implementation_services.login_postgres_service import LoginPostgresService

login_dao = LoginPostgresDAO()
login_service = LoginPostgresService(login_dao)

username = "username"
password = "password"


def test_validate_correct_credentials():
    validation = login_service.validate_login(username, password)
    assert validation


def test_catch_bad_username():
    validation = login_service.validate_login('bad username', password)
    if validation:
        assert False
    else:
        assert True


def test_catch_bad_password():
    validation = login_service.validate_login(username, 'bad password')
    if validation:
        assert False
    else:
        assert True


def test_catch_bad_username_and_password():
    validation = login_service.validate_login('bad username', 'bad password')
    if validation:
        assert False
    else:
        assert True
