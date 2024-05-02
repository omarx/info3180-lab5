from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from .config import Config
import os

app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, '..', 'uploads')

from app import models
from .forms import MovieForm

from .models import Movies, db
from app import views
