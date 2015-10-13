from flask import render_template, flash, redirect, session, url_for, request, g, jsonify, send_from_directory, Response
from datetime import datetime, timedelta
from functools import wraps, partial
import os
import unicodedata
import random
import string
import time
import base64
import unicodedata
import re
import io
import tempfile
import json
import pickle

from wtforms.validators import ValidationError
from jinja2 import Markup
from app import app

# ===========================================================
# init code
# ===========================================================

# app.logger.info( app.config['COREDB_DATABASE_URI'] )
app.secret_key = app.config['SECRET_KEY']
app.jinja_env.globals['include_raw'] = lambda filename : Markup(app.jinja_loader.get_source(app.jinja_env, filename)[0])
APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
APP_STATIC = os.path.join(APP_ROOT, 'static')

#============================================================
# routes
#============================================================
    
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/movie')
def page_index():
    with open( os.path.join( APP_ROOT, 'templates', 'movie.html') ) as f:
        return Response(f.read(), status=200, mimetype='text/html')
    
@app.route('/partials/<partial_file>')
def get_partial_file(partial_file):
    with open( os.path.join( APP_ROOT, 'templates/partials', partial_file ) ) as f:
        return Response(f.read(), status=200, mimetype='text/html')

#============================================================
# services
#============================================================
    
entries = None
pickle_file_name = os.path.join( tempfile.gettempdir(), 'entries.pickle' )
if os.path.exists(pickle_file_name):
    try:
        with open(pickle_file_name,'rb') as f:
            entries = pickle.load(f)
    except Exception as e:
        app.logger.error('Exception loading persisted storage %s', e)
if not entries:
    entries = []
    for x in range(10):
        entries.append({'id':str(x),'_id':str(x),'title':'title for {}'.format(x),'director':'Direction robot #{}'.format(x),'releaseYear':x+2000,'genre':'independent'})
    
def persist():
    with open(pickle_file_name,'wb') as f:
        pickle.dump(entries,f)
    
@app.route('/api/entries/<id>', methods=['GET','PUT','DELETE'])
def api_entries_deal_with_one(id):
    app.logger.info('api_entries_deal_with_one %s', id)
    fields = ['title','genre','director','releaseYear']
    for index, e in enumerate(entries):
        if e['id'] == id:
            if request.method == 'GET':
                return Response(json.dumps(e), status=200, mimetype='application/json')
                
            if request.method == 'PUT':
                for f in fields:
                    e[f] = request.json[f]
                persist()
                return 'ok'
                
            if request.method == 'DELETE':
                del entries[index]
                persist()
                return 'ok'

    abort(404)

    
@app.route('/api/entries', methods=['GET','POST'])
def api_entries_all_add():
    if request.method == 'GET':
        app.logger.info('get_all')
        # http://stackoverflow.com/a/20974518/72668
        return Response(json.dumps(entries), status=200, mimetype='application/json')
    # must be 'POST'
    app.logger.info('add_entry')
    fields = ['title','genre','director','releaseYear']
    e = {}
    id = str(random.randint(0,9999999))
    e['id'] = id
    e['_id'] = id
    for f in fields:
        e[f] = request.json[f]
    entries.append(e)
    persist()
    return id
    
           

# =======================================================================
# error handlers
# =======================================================================
    
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500
