from marshmallow import Schema, fields
from sqlalchemy import Column, String, Integer

from project.setup_db import db


class Director(db.Model):
    __tablename__ = 'director'
    id = Column(Integer(), primary_key=True)
    name = Column(String(255), unique=True, nullable=False)


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()
