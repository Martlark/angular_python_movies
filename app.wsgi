# http://flask.pocoo.org/docs/0.10/deploying/mod_wsgi/
import sys
sys.path.insert(0, '/var/www/Mega/')

from app import app as application
