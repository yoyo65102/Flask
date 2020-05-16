# ローカル環境
from config.base_setting import *
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "mysql://{user}:{password}@{host}:{port}/flaskbase".format(**{
    'user': 'flask',
    'password': '123456',
    'host': 'localhost',
    "port": "3306"
})
SECRET_KEY = "678910"
