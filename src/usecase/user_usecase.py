from src.infra.repository.user_repository import UserRepository


class UserUseCase:
    def create(self, user):
        UserRepository().commit(user)
