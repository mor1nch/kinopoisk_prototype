from marshmallow import Schema, fields
from sqlalchemy import Column, String, Integer

from project.setup_db import db


class Genre(db.session):
    __tablename__ = 'genres'
    id = Column(Integer(), primary_key=True)
    name = Column(String(100), unique=True, nullable=False)


class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()
