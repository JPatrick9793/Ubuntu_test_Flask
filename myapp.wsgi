#!/usr/bin/python
activate_this = '/var/www/myproject/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
import sys
sys.path.insert(0,"/var/www/")
from myproject import app as application
