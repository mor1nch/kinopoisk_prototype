from project.dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, gid: int) -> None or list:
        return self.dao.get_one(gid)

    def get_all(self) -> list:
        return self.dao.get_all()

    def create(self, genre_data: dict) -> None:
        return self.dao.create(genre_data)

    def update(self, genre_data: dict) -> None:
        self.dao.update(genre_data)

    def delete(self, gid: int) -> None:
        self.dao.delete(gid)
