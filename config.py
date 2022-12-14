import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(basedir, 'env'))
load_dotenv(os.path.join(basedir, 'flaskenv'))
class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'blog.db')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOAD_FOLDER = "static/img/posts"