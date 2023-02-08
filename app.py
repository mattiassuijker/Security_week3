import os.path
import sys
import datetime

from flask import Flask, jsonify, render_template, request, redirect
from functools import wraps

from lib.tablemodel import DatabaseModel

LISTEN_ALL = "0.0.0.0"
FLASK_IP = LISTEN_ALL
FLASK_PORT = 81
FLASK_DEBUG = True

app = Flask(__name__)
# This command creates the "<application directory>/databases/dummydata.db" path
DATABASE_FILE = os.path.join(app.root_path, 'databases', 'dummydata.db')