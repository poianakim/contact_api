from settings import *
import json

# initializing db with sqlalchemy class
db = SQLAlchemy(app)
# In termnal with python => import this db from this file(contacts) then db.create_all()


class Contact(db.Model):
    # __tablename__ = 'contacts'
    # produce id automatically
    id = db.Column(db.Integer, primary_key=True)
    first = db.Column(db.String(30), nullable=False)
    second = db.Column(db.String(30), nullable=True)
    number = db.Column(db.Integer,  nullable=False)

    #  convert data in json format
    def json(self):
        return {'id': self.id, 'firstname': self.first.capitalize(), 'secondname': self.second.capitalize(), 'number': self.number}

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

    def get_contact(_id):
        try:
            return Contact.json(Contact.query.filter_by(id=_id).first())
        except:
            return 'No Contact Found'

    def update_contact(_id, new_first, new_second, new_number):
        contact_update = Contact.query.filter_by(id=_id).first()
        contact_update.first = new_first
        contact_update.second = new_second
        contact_update.number = new_number
        db.session.commit()

    def delete_contact(_id):
        Contact.query.filter_by(id=_id).delete()
        db.session.commit()
