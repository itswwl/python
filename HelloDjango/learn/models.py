#from django.db import models
from django.forms import forms

# 1. 导入peewee的模块
from peewee import *
from datetime import datetime

import json

# Create your models here.

class AddForm(forms.Form):
    name = forms.Field(label="用户姓名",required=False)
    password = forms.Field(label="用户密码")


"""
class Person(models.Model):
    _table_ = "person"
    id = models.Field(primary_key=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
"""

# 2. 建立数据库实例
dbs = MySQLDatabase(
        database = 'python',
        host = 'localhost',
        port = 3306,
        user = 'root',
        passwd = '123',
        charset = 'utf8'
        )

# 3. 建立数据表的模型
# 4. 先建立基本模型，具体的模型在此基础上继承而来
class BaseModel(Model):
    class Meta:
        # 指定表所在的数据库
        database = dbs



class User(BaseModel):
    _table_ = "user"
    id = Field(primary_key=True)
    username = CharField()
    userage = CharField()
    userpawssword = CharField()
    userdate = DateField()

    def __hash__(self):
        return hash(self.id+self.username+self.userage+self.userpawssword+self.userdate)

    def __eq__(self, other):
        if self.id == other.id and self.username == other.username:
            return True
        return False

    """
    def __init__(self,username):
        self.username = username

    def getUsername(self):
        return self.username

    def setUsername(self,username):
        self.username = username

    """

    class Meta:
        database = dbs

"""
解决peewee 转json问题
http://stackoverflow.com/questions/21975920/peewee-model-to-json
"""
class MyModel(Model):

  def __str__(self):
    r = {}
    for k in self._data.keys():
      try:
         r[k] = str(getattr(self, k))
      except:
         r[k] = json.dumps(getattr(self, k))
    return str(r)

class Test(MyModel):
    #_table_ = "test"
    id = Field(primary_key=True)
    testname = CharField()
    testage = CharField()

    class Meta:
        database = dbs

class A:
    id = None
    name = None
    pwd = None
