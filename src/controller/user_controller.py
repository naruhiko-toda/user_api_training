from src.domain.model.user import User
from src.usecase.user_usecase import UserUseCase


class UserController:
    def create(self, params):
        try:
            UserUseCase().create(User(params))
        except ValueError as e:
            return {"status": 400, "error": e.args[0]}
        return {"status": 201}
