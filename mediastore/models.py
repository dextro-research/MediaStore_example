from mediastore import db
import datetime

def _get_date():
    return datetime.datetime.utcnow()
    
    

entities = db.Table('entities',
    db.Column('entity_id', db.Integer, db.ForeignKey('entity.id')),
    db.Column('media_id', db.Integer, db.ForeignKey('media.id')),
    db.PrimaryKeyConstraint('entity_id', 'media_id')
)
    

class Media(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    media_url = db.Column(db.String)
    entities = db.relationship('Entity', secondary=entities, backref=db.backref('media', lazy='dynamic'))
    created_at = db.Column(db.DateTime, default=_get_date)
    updated_at = db.Column(db.DateTime, onupdate=_get_date)
    
    
class Entity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String, unique=True)
    created_at = db.Column(db.DateTime, default=_get_date)
    updated_at = db.Column(db.DateTime, onupdate=_get_date)