# Python Flask REST CONTACT API with CRUD 

#### Default proxy -  [localhost:5000](http://localhost:5000/)

## Installation
1. Clone repo ``` git clone ...```
2. Create virtualenv ```python3 -m venv venv```
3. Install Flask and Flask SQLAlchey ```pip install flask Flask-SQLAlchemy```
4. Install SQLAlchemy sperately since ver 1.4.0 automatically included in Flask SQLAlchemy causes Assertion Error ```pip install SQLAlchemy==1.3.23```
5. Activate virtualenv ```source venv/bin/activate```
6. Outputs the packages and produce requirements.txt ```pip freeze > requirements.txt```
7. Create DB ```python3``` ```from contacts import db``` ```db.create_all()``` ```exit()```
8. Run in localhost ```python api.py```

### <USER STORIES>

You can "GET" a contact by id with
```
/contacts/<int:id>
```
Response will be like
```
{"firstname": "Micheal", "secondname": "Scott", "number": 128484848}
```
You can "GET" all contacts with
```
/contacts
```
Response will be like
```
[{{"firstname": "Micheal", "secondname": "Scott", "number": 128484848}
}, {"firstname": "Dwight", "secondname": "Schrut", "number": 11119999}]
```

You can "POST" a contact with
```
/add
```
You can PUT(UPDATE) a contact with id
You can DELETE a contact with id
```
/contacts/<int:id>
```
