from abc import ABC, abstractmethod


class LoginDAO(ABC):
    @abstractmethod
    def get_login_by_credentials(self, username: str, password: str):
        pass
