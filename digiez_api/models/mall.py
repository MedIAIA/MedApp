from marshmallow import fields
from digiez_api.extensions import db, ma
from . base_model import BaseModel, now


class Mall(db.Model, BaseModel):
    __tablename__ = 'malls'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    address = db.Column(db.String(300), unique=False, nullable=True)
    account_id = db.Column(db.Integer, db.ForeignKey("accounts.id",
                                                     ondelete='SET NULL'))
    units = db.relationship('Unit', lazy='joined')
    creation_date = db.Column(db.DateTime, default=now, nullable=False)
    last_modification_date = db.Column(db.DateTime, default=now, onupdate=now, nullable=False)

    def __init__(self, name, address=None, account_id=None, **kwargs):
        self.name = name
        self.address = address
        self.account_id = account_id


class MallSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    account_id = fields.Integer()
    address = fields.String(required=False)
    creation_date = fields.DateTime()
    last_modification_date = fields.DateTime()


mall_schema = MallSchema()
malls_schema = MallSchema(many=True)
