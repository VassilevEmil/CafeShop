from app import db


class VIACustomer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    address = db.Column(db.String(100))
    via_card_number = db.Column(db.String(20))

    # this method provides a human readable string representation
    def __repr__(self):
        return f"VIACustomer(id={self.id}, name={self.name}, address={self.address}, via_card_number={self.via_card_number}"
