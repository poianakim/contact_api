from flask import Flask, request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy
# sqlalchemy 1.4.0 version makes Assertion error so I down-graded it to the (previous) 1.3.x version

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

''' 
If set to True (the default) Flask-SQLAlchemy will track modifications of objects and emit signals. 
This requires extra memory and can be disabled if not needed
default is None but without setting to Fals the err msg keeps showing
'''
