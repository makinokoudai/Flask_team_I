from gas import db  
from datetime import datetime

class Gas(db.Model):
    __tablename__ = 'gases'
    id = db.Column(db.Integer, primary_key=True)
    car = db.Column(db.String(50))
    nenpi = db.Column(db.Float)
    price = db.Column(db.Integer)
    extra = db.Column(db.String(300))
    created_at = db.Column(db.DateTime)

    def __init__(self, car=None, nenpi=None, price=None, extra=None):
        self.car = car
        self.nenpi = nenpi
        self.price = price
        self.extra = extra
        self.created_at = datetime.utcnow()

    def __repr__(self):
        return '<Entry id:{} car:{} nenpi:{} price:{} extra:{}>'.format(self.id, self.car, self.nenpi, self.price, self.extra)