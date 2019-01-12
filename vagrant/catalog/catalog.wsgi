#!/usr/bin/python3
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/Catalog/Catalog-Deployment/vagrant/catalog/")

from  __init__ import app as application
application.secret_key = 'My Secret key'
