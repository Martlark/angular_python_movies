# source_query.py
# configuration file

DEBUG = False
TESTING = False
CSRF_ENABLED = True

WTF_CSRF_ENABLED = True
SECRET_KEY = 'lfkjdoicvq49487ctueojrruihveiuy4ihdflkfj'
    
import os
# cheap ass way of determining in development
if os.environ.get('USER') and os.environ['USER'] == 'vagrant':
    DEBUG = True
    
basedir = os.path.abspath(os.path.dirname(__file__))
#
# https://pythonhosted.org/Flask-SQLAlchemy/binds.html
#
# default
