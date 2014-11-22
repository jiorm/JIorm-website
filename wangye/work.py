#coding:gbk
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Template,Context
import datetime
from django.http import Http404, HttpResponse
import datetime
from Article.models import *
from django.db import connection
from django.core.paginator import *

def work(request):
    str="作品名称".decode('gbk')
    pic=Works.objects.filter(works_name=str)
    print pic
    return render_to_response("works.htm"{"path":pic.works_image})
