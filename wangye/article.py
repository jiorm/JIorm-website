#coding:gbk
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Template,Context
import datetime
from django.http import Http404, HttpResponse
from Article.models import *
from django.db import connection
from django.core.paginator import *

def passage(request):
    #cursor=connection.cursor()
    #cursor.execute('select * from article_psg')
    #psg=cursor.fetchall()
    psg=Psg.objects.all()
    #paginator = JuncheePaginator(psg, 8)
    after_range_num = 5        #��ǰҳǰ��ʾ5ҳ
 
    befor_range_num = 4       #��ǰҳ����ʾ4ҳ
 
    try:                     #��������ҳ������1�������ʹ�������ת����1ҳ
        page = int(request.GET.get("page",1))
 
        if page < 1:
            page = 1
    except ValueError:
        page = 1
    paginator = Paginator(psg,5)   # ����books��ÿҳ��ʾ������������Ϊ2
    try:                     #��ת������ҳ�棬�����ҳ�����ڻ��߳�������ת��βҳ
        psg_list = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
        psg_list = paginator.page(paginator.num_pages)
    if page >= after_range_num:
        page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
        page_range = paginator.page_range[0:int(page)+befor_range_num]
    return render_to_response("article.htm",{"passages":psg_list,
                                             "page_range":page_range})
def content(request):
#    if 'id' in request.GET:
#        id1=request.GET["id"]
#        psg=Psg.objects.get(id=id1)
    #cmt=Comment.objects.get(comment_psgid=psg.id)
    if 'name' in request.GET and 'message' in request.GET:
        id1=request.GET["id"]
        psg=Psg.objects.get(id=id1)
        na=request.GET['name']
        msg=request.GET['message']
        if len(Comment.objects.filter(comment_name=na,comment_comment=msg))!=0:
            cmttmp=Comment.objects.get(comment_name=na,comment_comment=msg)

            return HttpResponse("�����ظ��ύ��".decode('gbk'))
        else:
            p=Comment(comment_name=na,comment_comment=msg,comment_time=datetime.datetime.now(),comment_mark=0,comment_psgid=psg)
            p.save()
    if 'id' in request.GET:
        id1=request.GET["id"]
        psg=Psg.objects.get(id=id1)
        print psg.passage_num
        psg.passage_num=psg.passage_num+1
        print psg.passage_num
        psg.save()
    cmt=Comment.objects.filter(comment_psgid=psg)
    after_range_num = 5        #��ǰҳǰ��ʾ5ҳ
 
    befor_range_num = 4       #��ǰҳ����ʾ4ҳ
 
    try:                     #��������ҳ������1�������ʹ�������ת����1ҳ
        page = int(request.GET.get("page",1))
 
        if page < 1:
            page = 1
    except ValueError:
        page = 1
    paginator = Paginator(cmt,5)   # ����books��ÿҳ��ʾ������������Ϊ2
    try:                     #��ת������ҳ�棬�����ҳ�����ڻ��߳�������ת��βҳ
        cmt_list = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
        cmt_list = paginator.page(paginator.num_pages)
    if page >= after_range_num:
        page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
        page_range = paginator.page_range[0:int(page)+befor_range_num]

    return render_to_response("article2.htm",{"passage":psg,
                                              "comments":cmt_list,
                                              "page_range":page_range})
def work(request):
    pic=Works.objects.all()
    after_range_num = 5        #��ǰҳǰ��ʾ5ҳ
 
    befor_range_num = 4       #��ǰҳ����ʾ4ҳ
 
    try:                     #��������ҳ������1�������ʹ�������ת����1ҳ
        page = int(request.GET.get("page",1))
 
        if page < 1:
            page = 1
    except ValueError:
        page = 1
    paginator = Paginator(pic,5)   # ����books��ÿҳ��ʾ������������Ϊ2
    try:                     #��ת������ҳ�棬�����ҳ�����ڻ��߳�������ת��βҳ
        pic_list = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
        pic_list = paginator.page(paginator.num_pages)
    if page >= after_range_num:
        page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
        page_range = paginator.page_range[0:int(page)+befor_range_num]

    return render_to_response("work.htm",{"works":pic_list,
                                          "page_range":page_range})

