# 本番環境
from config.base_setting import *
SQLALCHEMY_ECHO = False
DEBUG = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "mysql://{user}:{password}@{host}:{port}/flaskbase".format(**{
    'user': 'flask',
    'password': 'ho;aHc5!',
    'host': '118.27.38.240',
    "port": "3306"
})
SECRET_KEY = "678910"
