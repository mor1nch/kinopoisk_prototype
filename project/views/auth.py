from flask import request
from flask_restx import Namespace, Resource
from project.container import auth_services
from project.container import user_services
from project.helpers.decorators import auth_required

auth_ns = Namespace("auth")


@auth_ns.route('/register')
class AuthViewRegister(Resource):
    @auth_required
    def post(self):
        req_json = request.json
        user_services.create(req_json)
        return 'Created', 201


@auth_ns.route('/login')
class AuthView(Resource):
    @auth_required
    def post(self):
        req_json = request.json
        email = req_json.get('email', None)
        password = req_json.get('password', None)

        if email is None or password is None:
            return 'Failed', 400
        tokens = auth_services.generate_token(email, password)
        return tokens, 201

    @auth_required
    def put(self):
        req_json = request.json
        refresh_token = req_json.get('refresh_token', None)

        if refresh_token is None:
            return '', 401

        tokens = auth_services.approve_refresh_token(refresh_token)
        return tokens, 201
