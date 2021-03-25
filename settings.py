from flask import Flask, request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
# sqlalchemy 1.4.0 version makes Assertion error so I downgraded it to the (previous) 1.3.x version

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route("/")
@cross_origin()
''' 
If set to True (the default) Flask-SQLAlchemy will track 
modifications of objects and emit signals. 
This requires extra memory and can be disabled if not needed
default is None but without setting to False the err msg keeps showing
'''
