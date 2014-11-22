#-*- coding:utf-8 -*-

import os
import sys
 
os.environ['DJANGO_SETTINGS_MODULE'] = 'wangye.settings'
 
path = os.path.dirname(os.path.abspath(__file__)) + '/wangye'
if path not in sys.path:
    sys.path.insert(1, path)
 
from django.core.handlers.wsgi import *
from bae.core.wsgi import WSGIApplication
 
application = WSGIApplication(WSGIHandler())
