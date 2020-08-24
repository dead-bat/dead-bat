import functools

from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
from db import get_db
# for below: first try commenting the above line and uncommenting the below
# from . import db # now change all instances of get_db() to db.get_db()
# NOTE: the above import (get_db) may throw an error if there is another module named db 
# somewhere else in the library. it needs to come from the will-code-for-coffee/db.py file
# but hyphens are forbidden for module names. either need work around or rename the directory
# (consider replacing the hyphens with underscores)

bp = Blueprint('auth', __name__, url_prefix='/auth')