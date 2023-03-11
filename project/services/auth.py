import datetime
import calendar
import jwt

from project.constants import JWT_SECRET, JWT_ALGORITHM
from project.services.user import UserService
from flask import abort


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def register_new_user(self, data: dict):
        return self.user_service.create(data)

    def generate_token(self, email: str, password: str, is_refresh=False) -> dict:
        user = self.user_service.get_by_email(email)

        if user is None:
            abort(404)

        if not is_refresh:
            if not self.user_service.compare_password(user.password, password):
                abort(404)

        data = {
            "email": user.email,
        }

        # 30 minutes for access_token
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

        # 130 days for refresh_token
        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

        tokens = {
            "access_token": access_token,
            "refresh_token": refresh_token
        }
        return tokens

    def approve_refresh_token(self, refresh_token: str) -> dict:
        data = jwt.decode(jwt=refresh_token, key=JWT_SECRET, algorithms=[JWT_ALGORITHM])

        email = data.get("email")
        user = self.user_service.get_by_email(email)

        if user is None:
            abort(404)

        return self.generate_token(email, user.password, is_refresh=True)
