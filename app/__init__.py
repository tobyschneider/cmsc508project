from flask import Flask
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from dbconnect import connection

app = Flask(__name__)
app.config['SECRET_KEY'] = '8fJy$eU$`Y.>[N5]'
bootstrap = Bootstrap(app)

from app import routes, forms
