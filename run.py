#!/usr/bin/python
from app import app
# see: http://stackoverflow.com/questions/23230599/having-problems-accessing-port-5000-in-vagrant
app.run(debug=True,host='0.0.0.0',port=5000)

