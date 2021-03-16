from settings import *
import json

# initializing db with sqlalchemy class
db = SQLAlchemy(app)


class Contact(db.Model):
    # __tablename__ = 'contacts'
    # produce id automatically
    id = db.Column(db.Integer, primary_key=True)
    first = db.Column(db.String(30), nullable=False)
    second = db.Column(db.String(30), nullable=True)
    number = db.Column(db.Integer,  nullable=False)

    #  convert data in json format
    def json(self):
        return {'name': self.first.capitalize() + ", " + self.second.capitalize(), 'number': self.number}

    def add_contact(_first, _second, _number):
        new_contact = Contact(first=_first.lower(),
                              second=_second.lower(), number=_number)
        db.session.add(new_contact)
        db.session.commit()

    def get_all_contacts():
        result = []
        for contact in Contact.query.all():
            result.append(Contact.json(contact))
        return result

    def get_contact(_first):
        result = []
        for contact in Contact.query.filter_by(first=_first).all():
            result.append(Contact.json(contact))
        return result

    def update_contact(_first, new_first, new_second, new_number):
        contact_update = Contact.query.filter_by(first=_first).first()
        contact_update.first = new_first
        contact_update.second = new_second
        contact_update.number = new_number
        db.session.commit()

    def delete_contact(_first):
        Contact.query.filter_by(first=_first).delete()
        db.session.commit()
