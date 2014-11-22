# -*- coding: gb2312 -*-

import MySQLdb
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Template,Context
import datetime
from django.http import Http404, HttpResponse
import datetime
from django.db import connection
from Article.models import *

def index(request):
    psg=Psg.objects.all()[:6]
    return render_to_response('index.htm',{'passages':psg})
    
