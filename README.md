# Python Flask REST CONTACT API with CRUD 

#### Default proxy -  [localhost:5000](http://localhost:5000/)
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