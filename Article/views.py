#coding:gbk
# Create your views here.
import MySQLdb
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Template,Context
import datetime
from django.http import Http404, HttpResponse
import datetime
from django.db import connection

def article(request):
    a='第一个app'.decode("gbk")
    return render_to_response("index.htm",{"content":a})
