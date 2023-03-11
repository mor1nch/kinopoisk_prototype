from project.dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, did: int) -> list[Director]:
        return self.session.query(Director).get(did)

    def get_all(self) -> list[Director]:
        return self.session.query(Director).all()

    def create(self, director_data: dict) -> None:
        new_director = Director(**director_data)

        self.session.add(new_director)
        self.session.commit()

    def update(self, director_data: dict) -> None:
        director = self.get_one(director_data.get("id"))
        director.name = director_data.get("name")

        self.session.add(director)
        self.session.commit()

    def delete(self, did: int) -> None:
        director = self.get_one(did)

        self.session.delete(director)
        self.session.commit()
