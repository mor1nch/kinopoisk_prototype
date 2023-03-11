from flask_restx import Resource, Namespace
from flask import request
from project.dao.model.genre import GenreSchema
from project.container import genre_services
from project.helpers.decorators import auth_required

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        all_genres = genre_services.get_all()
        return genres_schema.dump(all_genres), 200

    @auth_required
    def post(self):
        req_json = request.json
        genre = genre_services.create(req_json)
        return "Created", 201, {"location": f"/genres/{genre.id}"}


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    @auth_required
    def get(self, gid):
        genre = genre_services.get_one(gid)
        return genre_schema.dump(genre), 200

    @auth_required
    def put(self, gid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = gid
        genre_services.update(req_json)
        return "Updated", 204

    @auth_required
    def delete(self, gid):
        genre_services.delete(gid)
        return "Deleted", 204
