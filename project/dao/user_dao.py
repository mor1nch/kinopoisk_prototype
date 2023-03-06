from project.dao.base import BaseDAO
from project.dao.model.user import User


class UsersDAO(BaseDAO[User]):
    __model__ = User

    def __init__(self, session):
        self.session = session

    def get_one(self, uid: int) -> list[User]:
        return self.session.query(User).get(uid)

    def get_all(self) -> list[User]:
        return self.session.query(User).all()

    def create(self, user_data: dict) -> None:
        new_user = User(**user_data)

        self.session.add(new_user)
        self.session.commit()

    def delete(self, uid: int) -> None:
        user = self.get_one(uid)

        self.session.delete(user)
        self.session.commit()

    def update(self, data: dict) -> None:
        user = self.get_one(data.get("id"))

        user.email = data.get("email")
        user.password = data.get("password")
        user.name = data.get("name")
        user.surname = data.get("surname")
        user.favorite_genre = data.get("favorite_genre")

        self.session.add(user)
        self.session.commit()
