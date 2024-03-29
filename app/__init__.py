import os
from flask import Flask
from config import basedir

app = Flask(__name__)
app.config.from_object('config')

import logging
    
from logging.handlers import RotatingFileHandler
file_handler = RotatingFileHandler('/tmp/angular_test.log', 'a', 1 * 1024 * 1024, 10)
file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
app.logger.setLevel(logging.INFO)
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)
app.logger.info('vanila flask start')

from app import views

