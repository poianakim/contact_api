from contacts import *


@app.route('/contacts', methods=['GET'])
def get_contacts():
    return jsonify({'Contacts': Contact.get_all_contacts()})

# converter should be string / int


@app.route('/contacts/<first>', methods=['GET'])
def get_contact_by_name(first):
    _first = first.lower()
    contact = Contact.get_contact(_first)
    return jsonify({'Contact Found': contact})


@app.route('/add', methods=['POST'])
def add_contact():
    new_contact = request.get_json()
    print(new_contact)
    Contact.add_contact(
        new_contact['first'], new_contact['second'], new_contact['number'])
    # mimetype (3rd arg of Response function) is type header
    response = Response('Contact Added', 201, mimetype='application/json')
    return response


@app.route('/contacts/<string:first>', methods=['PUT'])
def update_contact(first):
    _first = first.lower()
    new_contact = request.get_json()
    Contact.update_contact(
        _first, new_contact['first'], new_contact['second'], new_contact['number'])
    response = Response('Contact Updated', 200, mimetype='application/json')
    return response


@app.route('/contacts/<string:first>', methods=['DELETE'])
def delete_contact(first):
    _first = first.lower()
    Contact.delete_contact(_first)
    response = Response('Contact Deleted', 200, mimetype='application/json')
    return response


if __name__ == "__main__":
    app.run(debug=False)
