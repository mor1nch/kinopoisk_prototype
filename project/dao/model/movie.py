from marshmallow import Schema, fields
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from project.dao.model.genre import Genre
from project.dao.model.director import Director

from project.setup.db import models


class Movie(models.Base):
    __tablename__ = 'movies'
    id = Column(Integer(), primary_key=True)
    title = Column(String(), nullable=False)
    description = Column(String())
    trailer = Column(String())
    year = Column(Integer())
    rating = Column(Float())
    genre_id = Column(Integer(), ForeignKey(Genre.id))
    director_id = Column(Integer(), ForeignKey(Director.id))
    genre = relationship("Genre")
    director = relationship("Director")


class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Integer()
    director_id = fields.Integer()