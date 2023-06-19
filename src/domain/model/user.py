from src.domain.model.tel import Tel


class User:
    def __init__(self, params):
        self.__validate(params)
        self.name = params.get("name")
        self.tel = Tel(params.get("tel"))

    def __validate(self, params):
        if not params.get("name"):
            raise ValueError("name is required")
