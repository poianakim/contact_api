from contacts import *

# get all the contacts data


@app.route('/contacts', methods=['GET'])
def get_contacts():
    return jsonify(Contact.get_all_contacts())

# get single data with id


@app.route('/contacts/<int:id>', methods=['GET'])
def get_contact_by_name(id):
    contact = Contact.get_contact(id)
    return jsonify(contact)


# add a contact data
@app.route('/add', methods=['POST'])
def add_contact():
    new_contact = request.get_json()
    Contact.add_contact(
        new_contact['first'], new_contact['second'], new_contact['number'])
    # mimetype (3rd arg of Response function) is header content type
    response = Response('Contact Added', 201, mimetype='application/json')
    return response


# update a contact data selected by id
@app.route('/contacts/<int:id>', methods=['PUT'])
def update_contact(id):
    new_contact = request.get_json()
    Contact.update_contact(
        id, new_contact['first'], new_contact['second'], new_contact['number'])
    response = Response('Contact Updated', 200, mimetype='application/json')
    return response


# delete a contact data selected by id
@app.route('/contacts/<int:id>', methods=['DELETE'])
def delete_contact(id):
    Contact.delete_contact(id)
    response = Response('Contact Deleted', 200, mimetype='application/json')
    return response


if __name__ == "__main__":
    app.run(debug=False)
