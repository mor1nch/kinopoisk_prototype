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
        did = director_data.get('id')
        director = self.get_one(did)
        director.name = director_data.get('name')

        self.dao.update(director)

    def delete(self, did: int) -> None:
        self.dao.delete(did)
