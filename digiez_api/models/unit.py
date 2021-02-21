from marshmallow import fields
from digiez_api.extensions import db, ma
from . base_model import BaseModel, now


class Unit(db.Model, BaseModel):
    __tablename__ = 'units'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    manager = db.Column(db.String(150), unique=False, nullable=True)
    mall_id = db.Column(db.Integer, db.ForeignKey("malls.id",
                                                  ondelete='SET NULL'))
    creation_date = db.Column(db.DateTime, default=now, nullable=False)
    last_modification_date = db.Column(db.DateTime, default=now, onupdate=now, nullable=False)

    def __init__(self, name, manager=None, mall_id=None, **kwargs):
        self.name = name
        self.manager = manager
        self.manager = mall_id

class UnitSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    manager = fields.String(required=False)
    mall_id = fields.Integer()
    creation_date = fields.DateTime()
    last_modification_date = fields.DateTime()



unit_schema = UnitSchema()
units_schema = UnitSchema(many=True)
