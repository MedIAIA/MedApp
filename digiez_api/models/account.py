from marshmallow import fields
from digiez_api.extensions import db, ma
from . base_model import BaseModel, now


class Account(db.Model, BaseModel):
    __tablename__ = 'accounts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    phone = db.Column(db.String(12), unique=False, nullable=True)
    malls = db.relationship('Mall')
    creation_date = db.Column(db.DateTime, default=now, nullable=False)
    last_modification_date = db.Column(db.DateTime, default=now, onupdate=now, nullable=False)

    def __init__(self, name, phone=None, **kwargs):
        self.name = name
        self.phone = phone

class AccountSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    phone = fields.String(required=False)
    creation_date = fields.DateTime()
    last_modification_date = fields.DateTime()


account_schema = AccountSchema()
accounts_schema = AccountSchema(many=True)
