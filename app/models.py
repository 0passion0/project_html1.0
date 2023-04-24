from django.db import models
# Create your models here.m
class Userment(models.Model):
    id = models.CharField(verbose_name='学号',max_length=11,primary_key=True)
    name=models.CharField(verbose_name='姓名',max_length=16)
    #Tid = models.ForeignKey(to='Deartment', to_field="id", null=True,blank=True,on_delete=models.SET_NULL)#不级联删除
    gender = models.CharField(verbose_name="性别",max_length=5)
    math=models.IntegerField(verbose_name='数学')
    python = models.IntegerField(verbose_name='python')
    C = models.IntegerField(verbose_name='C')
    coun = models.IntegerField(verbose_name='总分')
class Survey(models.Model):
    # 个人信息
    q1_1 = models.IntegerField(null=True, blank=True)
    q1_2 = models.CharField(max_length=10, null=True, blank=True)
    q1_3 = models.CharField(max_length=50, null=True, blank=True)

    # 问题 2runserver
    q2_1 = models.BooleanField(null=True, blank=True)
    q2_2 = models.BooleanField(null=True, blank=True)
    q2_3 = models.BooleanField(null=True, blank=True)
    q2_4 = models.BooleanField(null=True, blank=True)

    # 问题 3
    q3_1 = models.CharField(max_length=50, null=True, blank=True)
    q3_2 = models.CharField(max_length=50, null=True, blank=True)
    q3_3 = models.CharField(max_length=50, null=True, blank=True)
    q3_4 = models.TextField(null=True, blank=True)
    q3_5 = models.TextField(null=True, blank=True)

    # 问题 4
    q4_1 = models.CharField(max_length=50, null=True, blank=True)
    q4_2 = models.BooleanField(null=True, blank=True)
    q4_3 = models.CharField(max_length=100, null=True, blank=True)
    q4_4 = models.BooleanField(null=True, blank=True)
    q4_5 = models.TextField(null=True, blank=True)

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=100)


"""python manage.py makemigrations
python manage.py migrate
"""
