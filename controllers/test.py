from flask import Blueprint, render_template
from common.models.user import User

test_page = Blueprint("test_page", __name__)


@test_page.route("/")
def hello():
  return render_template('main.html')

@test_page.route("/visugi")
def whisky():
  return render_template('visugi.html')

@test_page.route("/biru")
def bear():
  return render_template('biru.html')

@test_page.route("/wain")
def wine():
  return render_template('wain.html')

@test_page.route("/yuri")
def love():
  return "LOVE"

@test_page.route("/index")
def index():
   return render_template('index.html')
