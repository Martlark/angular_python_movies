#===================
#install script for query
#Andrew Rowe 6-13-2015
#run as sudo
#Copyright (c) 1-Page
#===================
#apache2
apt-get -q -y install apache2
#unzip
apt-get -q -y install unzip
#python 
apt-get -q -y install libapache2-mod-wsgi python-dev
apt-get -q -y install python-pip
pip install Flask
#basic authorisation
apt-get -q -y install apache2-utils
pip install Flask-BasicAuth
pip install flask-rauth
pip install flask-sqlalchemy
pip install flask
pip install flask-login
pip install flask-mail
pip install sqlalchemy-migrate
pip install flask-whooshalchemy
pip install flask-wtf
pip install coverage
pip install flask-mail
pip install gevent
pip install celery
pip install redis
apt-get -q -y install redis-server
apt-get -q -y install python-psycopg2
#install git
apt-get -q -y install git
echo Complete.
#all done
