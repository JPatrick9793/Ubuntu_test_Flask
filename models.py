from myproject import db

class Places(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String())
    city = db.Column(db.String())
    country = db.Column(db.String())
    def __repr__(self):
        return '<city %r>' % (self.city)

db.create_all()
