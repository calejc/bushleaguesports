from flask import Flask
from flask_cors import CORS;
from flask_scss import Scss

app = Flask(__name__, instance_relative_config=True)
app.debug=True
CORS(app)
Scss(app, static_dir='app/static', asset_dir='app/assets/styles')

from app import views

app.config.from_object('config')