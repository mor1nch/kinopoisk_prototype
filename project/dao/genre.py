from project.dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, gid: int) -> list[Genre]:
        return self.session.query(Genre).get(gid)

    def get_all(self) -> list[Genre]:
        return self.session.query(Genre).all()

    def create(self, genre_data: dict) -> None:
        new_genre = Genre(**genre_data)

        self.session.add(new_genre)
        self.session.commit()

    def update(self, genre_data: dict) -> None:
        genre = self.get_one(genre_data.get("id"))
        genre.name = genre_data.get("name")

        self.session.add(genre)
        self.session.commit()

    def delete(self, gid: int) -> None:
        genre = self.get_one(gid)

        self.session.delete(genre)
        self.session.commit()
