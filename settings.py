from flask import Flask, request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy
# sqlalchemy 1.4.0 version makes Assertion error so I downgraded it to the 1.3.x version

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
