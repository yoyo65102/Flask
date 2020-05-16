from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)

manager = Manager(app)
app.config.from_pyfile("config/base_setting.py")

# linux export ops_config=local|production
# windows set ops_config=local|production
# import pdb; pdb.set_trace()
os.environ['ops_config'] = 'local'
if "ops_config" in os.environ:
    app.config.from_pyfile("config/%s_setting.py" % (os.environ['ops_config']))

db = SQLAlchemy(app)
