from marshmallow import Schema, fields
from sqlalchemy import Column, String, Integer

from project.setup.db import models


class Genre(models.Base):
    __tablename__ = 'genres'
    id = Column(Integer(), primary_key=True)
    name = Column(String(100), unique=True, nullable=False)


class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()
