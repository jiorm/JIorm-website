# coding:gbk
from django.db import models

# Create your models here.
class Psg(models.Model):
    passage_title=models.CharField(max_length=20)
    passage_content=models.TextField()
    passage_abstract=models.TextField()
    passage_author=models.CharField(max_length=5)
    passage_time=models.DateTimeField()
    passage_num=models.IntegerField()
    passage_mark=models.IntegerField()
    def __unicode__(self):
        return self.passage_title
class Comment(models.Model):
    comment_name=models.CharField(max_length=10)
    comment_comment=models.CharField(max_length=200)
    comment_time=models.DateTimeField()
    comment_mark=models.IntegerField()
    comment_psgid=models.ForeignKey(Psg,related_name='psg_cmt')
    def __nuicode__(self):
        return self.comment_name
class Works(models.Model):
    works_name=models.CharField(max_length=20)
    works_author=models.CharField(max_length=10)
    works_content=models.TextField()
    works_abstract=models.CharField(max_length=60)
    works_image=models.FileField(upload_to="works")
    works_doc=models.FileField(upload_to="works")
    works_time=models.DateTimeField()
    def __unicode__(self):
        return self.works_name
class Contact(models.Model):
    contact_proname=models.CharField(max_length=15)
    contact_proaddress=models.CharField(max_length=20)
    contact_survey=models.TextField()
    contact_people=models.CharField(max_length=10)
    contact_position=models.CharField(max_length=10)
    contact_phone=models.CharField(max_length=11)
    contact_email=models.EmailField()
    def __unicode__(self):
        return self.contact_proname
class News(models.Model):
    news_title=models.CharField(max_length=100)
    news_urls=models.URLField()
    def __unicode__(self):
        return self.news_title


    

