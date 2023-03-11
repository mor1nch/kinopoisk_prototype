from project.dao.director import DirectorDAO
from project.dao.genre import GenreDAO
from project.dao.movie import MovieDAO
from project.dao.user import UserDAO
from project.services.auth import AuthService
from project.services.director import DirectorService
from project.services.genre import GenreService
from project.services.movie import MovieService
from project.services.user import UserService
from project.setup_db import db

genre_dao = GenreDAO(session=db.session)
genre_services = GenreService(dao=genre_dao)

director_dao = DirectorDAO(session=db.session)
director_services = DirectorService(dao=director_dao)

movie_dao = MovieDAO(session=db.session)
movie_services = MovieService(dao=movie_dao)

user_dao = UserDAO(db.session)
user_services = UserService(user_dao)

auth_services = AuthService(user_services)
