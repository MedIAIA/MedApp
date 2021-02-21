import datetime
from flask import current_app
from digiez_api.extensions import db


def now():
    return datetime.datetime.utcnow()


class BaseModel:

    def save(self, commit=True):
        try:
            if not self.id:
                db.session.add(self)
            if not commit:
                db.session.flush()
            else:
                db.session.commit()
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(' | '.join(['Error on save', repr(e)]))

    def update(self, data):
        self.__init__(**data)
        return self

    @classmethod
    def delete(cls, obj_id):
        deleted_count = cls.query.filter(cls.id == obj_id).delete()
        db.session.commit()
        return deleted_count
