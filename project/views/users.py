from flask_restx import Namespace, Resource
from project.container import user_services
from project.dao.model.user import UserSchema
from flask import request

from project.helpers.decorators import auth_required

user_ns = Namespace("users")

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route("/")
class UsersView(Resource):
    # @auth_required
    def get(self):
        return users_schema.dump(user_services.get_all()), 200

    # @auth_required
    def post(self):
        req_data = request.json
        user_services.create(req_data)
        return "", 201


@user_ns.route("/<int:uid>")
class UserView(Resource):
    # @auth_required
    def get(self, uid):
        return user_schema.dump(user_services.get_one(uid)), 200

    # @auth_required
    def patch(self, uid):
        data = request.json
        user_services.update(data, uid)
        return "Updated", 204


@user_ns.route("/password/<int:uid>")
class UserViewPassword(Resource):
    # @auth_required
    def put(self, uid):
        data = request.json
        user_services.update(data, uid)
        return "Updated", 204
