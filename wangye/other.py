#coding:gbk
import MySQLdb
import time
from django.shortcuts import render_to_response
from django.template import Template,Context
from django.http import Http404, HttpResponse
from django.db import connection
from Article.models import *
import urllib2,re
from sgmllib import SGMLParser
import os
import logging
from Article import pybcs 

staticTime=1416066132.62
request=urllib2.Request(url="http://www.ithome.com/")
result=urllib2.urlopen(request).read()
f=u'<span class="title"><a target="_blank" href='.encode('gb2312')
s=u'"[a-zA-z]+://[^\s]*">'.encode('gb2312')
t=u'[\s\S]*?</a></span></li>'.encode('gb2312')
pattern = re.compile(f+s+t)
search=pattern.findall(result)
results=''
for sear in search[:30]:
    results=results+sear
class NewsIt(SGMLParser):
    urls = []
    txt=[]
    #flag=0;
    def handle_data(self,text):
        #self.flag=1
        self.txt.append(text)
    def do_a(self, attrs):
        #if self.flag==0:
        #    return
        #else:
        for name, value in attrs:
            if name == 'href' and value not in self.urls:
                if value.startswith('http'):
                    self.urls.append(value)
                    #print value
            else:
                continue
        return
def newsget(request):
    flag=0
    p=NewsIt()
    p.feed(results)
    title=""
    url=""
    #url="http://www.baidu.com"
    for i in range(len(p.txt)):
        #newsDic[p.txt[i]]=p.urls[i]
        title=p.txt[i].decode("gbk")
        url=p.urls[i]
        itNews=News(news_title=title,news_urls=url)
        itNews.save()
        flag=1
    if flag==1:
        return HttpResponse("Success!")
    else:
        return HttpResponse("Not Success!")
def join(request):
    return render_to_response("join.htm")
def dosome(request):
    return render_to_response("dosome.htm")
def dynamic(request):
    return render_to_response("dynamic.htm")
def whoami(request):
    return render_to_response("whoami.htm")
def contactus(request):
    return render_to_response("contactus.htm")
def team(request):
    return render_to_response("team.html")
def newslist(request):
    new=News.objects.all()
    #print len(new)
    rNews=new[len(new)-30:len(new)]
    lNews=new[len(new)-59:len(new)-29]
    #print len(rNews)
    #print len(lNews)
    return render_to_response("news.html",{"newsleft":lNews,
                                           "newsright":rNews})
def send(request):
    try:
        ctc_pna=request.GET['field1']
        ctc_adr=request.GET['field2']
        ctc_sur=request.GET['field3']
        ctc_peo=request.GET['field4']
        ctc_pos=request.GET['field5']
        ctc_pho=request.GET['field6']
        ctc_ema=request.GET['field7']
        cta=Contact(contact_proname=ctc_pna,contact_proaddress=ctc_adr,contact_survey=ctc_sur,contact_people=ctc_peo,contact_position=ctc_pos,contact_phone=ctc_pho,contact_email=ctc_ema)
        cta.save()
    except ValueError:
        return render_to_response("<b>请填写完整!</b>".decode('gbk'))
    str="提交成功".decode('gbk')
    return HttpResponse("<body>"+str+"</body>")
