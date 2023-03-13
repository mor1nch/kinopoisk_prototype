from marshmallow import Schema, fields
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from project.dao.model.genre import Genre
from project.dao.model.director import Director

from project.setup_db import db


class Movie(db.Model):
    __tablename__ = 'movie'
    id = Column(Integer(), primary_key=True)
    title = Column(String(), nullable=False)
    description = Column(String(), nullable=False)
    trailer = Column(String(), nullable=False)
    year = Column(Integer(), nullable=False)
    rating = Column(Float(), nullable=False)
    genre_id = Column(Integer(), ForeignKey(Genre.id), nullable=False)
    director_id = Column(Integer(), ForeignKey(Director.id), nullable=False)
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
