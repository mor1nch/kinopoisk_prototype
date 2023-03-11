from sqlalchemy import desc

from project.dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid: int) -> list[Movie]:
        return self.session.query(Movie).get(mid)

    def get_all(self) -> list[Movie]:
        return self.session.query(Movie).all()

    def get_by_director_id(self, director_id: int) -> list[Movie]:
        return self.session.query(Movie).filter(Movie.director_id == director_id).all()

    def get_by_genre_id(self, genre_id: int) -> list[Movie]:
        return self.session.query(Movie).filter(Movie.genre_id == genre_id).all()

    def get_by_year(self, year: int) -> list[Movie]:
        return self.session.query(Movie).filter(Movie.year == year).all()

    def get_by_status(self):
        return self.session.query(Movie).order_by(desc(Movie.year))

    def create(self, movie_data: dict) -> None:
        new_movie = Movie(**movie_data)

        self.session.add(new_movie)
        self.session.commit()

    def update(self, movie_data: dict) -> None:
        movie = self.get_one(movie_data.get("id"))

        movie.title = movie_data.get("title")
        movie.description = movie_data.get("description")
        movie.trailer = movie_data.get("trailer")
        movie.year = movie_data.get("year")
        movie.rating = movie_data.get("rating")
        movie.genre_id = movie_data.get("genre_id")
        movie.director_id = movie_data.get("director_id")

        self.session.add(movie)
        self.session.commit()

    def delete(self, mid: int) -> None:
        movie = self.get_one(mid)

        self.session.delete(movie)
        self.session.commit()
