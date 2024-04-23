from app import db


class CreditCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    card_number = db.Column(db.String(16))
    expiry_date = db.Column(db.String(10))
    cvv = db.Column(db.String(4))

    def __repr__(self):
        return f"CreditCard(id={self.id}, card_number={self.card_number}, expiry_date={self.expiry_date}, cvv={self.cvv})"
