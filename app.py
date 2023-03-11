from flask import Flask
from flask_restx import Api

from project.config import Config
from project.setup_db import db
from project.views.directors import director_ns
from project.views.genres import genre_ns
from project.views.movies import movie_ns
from project.views.users import user_ns
from project.views.auth import auth_ns

api = Api(doc='/docs')


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    api.init_app(app)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
