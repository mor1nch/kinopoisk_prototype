from flask_restx import Resource, Namespace
from project.dao.model.director import DirectorSchema
from project.container import director_services
from flask import request
from project.helpers.decorators import auth_required

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):
        all_directors = director_services.get_all()
        return directors_schema.dump(all_directors), 200

    @auth_required
    def post(self):
        req_json = request.json
        director = director_services.create(req_json)
        return "Added", 201, {"location": f"/directors/{director.id}"}


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    @auth_required
    def get(self, did):
        director = director_services.get_one(did)
        return director_schema.dump(director), 200

    @auth_required
    def put(self, did):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = did
        director_services.update(req_json)
        return "Updated", 204

    @auth_required
    def delete(self, did):
        director_services.delete(did)
        return "Deleted", 204
