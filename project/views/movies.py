from flask_restx import Resource, Namespace
from project.container import movie_services
from flask import request
from project.helpers.decorators import auth_required
from project.dao.model.movie import MovieSchema

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    # @auth_required
    def get(self):
        year = request.args.get('year')
        status = request.args.get('status')
        page = request.args.get('page')
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')

        filters = {
            "year": year,
            "status": status,
            "page": page,
            "director_id": director_id,
            "genre_id": genre_id,
        }

        all_movies = movie_services.get_all(filters)
        return movies_schema.dump(all_movies), 200

    # @auth_required
    def post(self):
        req_json = request.json
        movie_services.create(req_json)
        return "Created", 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    # @auth_required
    def get(self, mid):
        movie = movie_services.get_one(mid)
        return movie_schema.dump(movie), 200

    # @auth_required
    def put(self, mid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = mid
        movie_services.update(req_json)
        return "Updated", 204

    # @auth_required
    def patch(self, mid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = mid
        movie_services.update(req_json)
        return "Updated", 204

    # @auth_required
    def delete(self, mid):
        movie_services.delete(mid)
        return "Deleted", 204
