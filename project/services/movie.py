from project.dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, mid: int) -> None or list:
        return self.dao.get_one(mid)

    def get_all(self, movie_data: dict) -> list:
        if movie_data.get("director_id") is not None:
            movies = self.dao.get_by_director_id(movie_data.get("director_id"))
        elif movie_data.get("genre_id") is not None:
            movies = self.dao.get_by_genre_id(movie_data.get("genre_id"))
        elif movie_data.get("year") is not None:
            movies = self.dao.get_by_year(movie_data.get("year"))
        elif movie_data.get("status") is not None and movie_data['status'] == 'new':
            movies = self.dao.get_by_status()
        else:
            movies = self.dao.get_all()

        if movie_data.get('page') is not None:
            return movies.limit(12).offset((int(movie_data.get('page')) - 1) * 12).all()
        return movies

    def create(self, movie_data: dict) -> None:
        return self.dao.create(movie_data)

    def update(self, movie_data: dict) -> None:
        return self.dao.update(movie_data)

    def delete(self, mid: int) -> None:
        self.dao.delete(mid)
