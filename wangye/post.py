import MySQLdb
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Template,Context
import datetime
from django.http import Http404, HttpResponse
from django.db import connection
from Article.models import *
import os
import logging
from Article import pybcs

def uploadFile(request):
    file1=request.FILES['photo']
    FileName=file1.name
    HOST = 'http://bcs.duapp.com/'
    AK = os.environ['AK']='wsD1d1F25EHzAXrAHZhU7aFf'
    SK = os.environ['SK']='65u3oIww4btR5yD3rYrnumhC4Cugh7aF'
    BUCKET='jiorm2'
    bcs=pybcs.BCS(HOST, AK, SK, pybcs.HttplibHTTPC)
    b=bcs.bucket(BUCKET)
    b.make_public()
    o=b.object(FileName)
    o.put_file(file1)
    re=HttpResponse()
    re['Content-Type']="application/json"
    imgurl="http://bcs.duapp.com/jiorm2/document%2F%28JPK487%7ES7W%28%5D%7DG%24ABN6%5DXF.jpg"
    json = "{\"status\":\"success\", \"imgurl\":\"" + imgurl + "\"}"  
    response.write(json)
    return re
def upload(request):
    if "photo" in request.FILES:
        file1=request.FILES['photo']
        FileName=file1.name
        HOST = 'http://bcs.duapp.com/'
        AK = os.environ['AK']='wsD1d1F25EHzAXrAHZhU7aFf'
        SK = os.environ['SK']='65u3oIww4btR5yD3rYrnumhC4Cugh7aF'
        BUCKET='jiorm2'
        bcs=pybcs.BCS(HOST, AK, SK, pybcs.HttplibHTTPC)
        b=bcs.bucket(BUCKET)
        b.make_public()
        o=b.object(FileName)
        o.put_file(file1)
        re=HttpResponse()
        re['Content-Type']="application/json"
        imgurl="http://bcs.duapp.com/jiorm2/"+FileName
    else :
        imgurl=""
    return render_to_response("post.html",{'src':imgurl})
