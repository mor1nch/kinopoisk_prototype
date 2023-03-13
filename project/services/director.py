from project.dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, did: int) -> None or list:
        return self.dao.get_one(did)

    def get_all(self) -> list:
        return self.dao.get_all()

    def create(self, director_data: dict) -> None:
        return self.dao.create(director_data)

    def update(self, director_data: dict) -> None:
        self.dao.update(director_data)

    def delete(self, did: int) -> None:
        self.dao.delete(did)
