from marshmallow import Schema, fields
from sqlalchemy import Column, String, Integer

from project.setup_db import db


class User(db.Model):
    __tablename__ = 'user'
    id = Column(Integer(), primary_key=True)
    email = Column(String(), unique=True, nullable=False)
    password = Column(String(), nullable=False)
    name = Column(String())
    surname = Column(String())
    favorite_genre = Column(String())


class UserSchema(Schema):
    id = fields.Int()
    email = fields.Str()
    password = fields.Str()
    name = fields.Str()
    surname = fields.Str()
    favorite_genre = fields.Str()
