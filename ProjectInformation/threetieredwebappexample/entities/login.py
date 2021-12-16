class Login:
    def __init__(self, username: str, password: str):
        self.login_id = 0
        self.username = username
        self.password = password

    def __str__(self):
        return f"id: {self.login_id}, username: {self.username}, password: *******"

    def login_to_dictionary(self):
        return {
            "loginId": self.login_id,
            "username": self.username,
            "password": self.password
        }
