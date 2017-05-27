from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from learn.models import AddForm

from learn.models import User
#from learn.models import db
from learn.models import Test

from learn.models import A

#import pymysql

from peewee import *
from learn.DBUtils import *

from django.http import HttpResponse
from django.http import JsonResponse



#导入时间
import time




#导入json
import json

#导入序列化对象
import  pickle

from playhouse.shortcuts import model_to_dict, dict_to_model

"""


# Create your views here.
def connDB(): #连接数据库函数
    conn=pymysql.connect(host='localhost',user='root',passwd='123',db='python',charset='utf8')
    cur=conn.cursor();
    return (conn,cur);

def exeUpdate(cur,sql):#更新语句，可执行update,insert语句
    sta=cur.execute(sql);
    return(sta);

def exeDelete(cur,IDs): #删除语句，可批量删除
    for eachID in IDs.split(' '):
        str = "delete from Person where id =" + eachID
        #print(str+)
        sta=cur.execute(str);
    return (sta);

def exeQuery(cur,sql):#查询语句
    cur.execute(sql);
    # print(sql)
    return (cur);

def connClose(conn,cur):#关闭所有连接
    cur.close();
    conn.commit()
    conn.close();
#调用连接数据库的函数
conn,cur=connDB();
"""
conn,cur=connDB();
def home(request):

    name = request.GET.get('name','wanglin')
    age = 123

    print("===================="+name+"==================")
    #conn1 = pymysql.connect(host='localhost', user='root', passwd='123', port=3306, charset='utf8')
    #cur1 = conn.cursor()  # 获取一个游标对象

    #cur1.execute("SELECT * FROM Person where name like'%"+name+"%'")
    #data = cur1.fetchall()

    #for row in data:
    #age = row[1]

    #cur1.close()  # 关闭游标
    #conn1.commit()  # 向数据库中提交任何未解决的事务，对不支持事务的数据库不进行任何操作
    #conn1.close()

    #sql = "SELECT * FROM Person where name like'%"+name+"%'";
    print("++++++++++++++++++++++++++++++")
    sql = "select * from person where name = '" + name + "'";
    print(sql)
    print("++++++++++++++++++++++++++++++")
    exeQuery(cur, sql);
    info = cur.fetchall();
    print(info)
    """
    for each in cur:
        age = each[1]
    """

        #print(age)
    #return render(request, 'home.html',{'name':name,'age':age})
    return render(request, 'home.html', {'info': info})

#删除操作
def delete(request):
    id = request.POST['id']
    print("======================================")
    print(id)
    sta = exeDelete(cur,id)
    connClose(conn, cur);
    print(sta)
    return render(request,'delete.html',{'msg':'success','status':sta})

#修改操作
def update(request):
    id = request.GET.get('id',0)
    name = request.GET.get('name','test')
    sta = exeUpdate(cur, "update Person set name = "+name+"where id =" + id );
    return render(request,'update.html',{'status':sta})

#添加操作
def insert(request):
    name = request.GET.get('name', 'test')
    age = request.GET.get('age', 12)
    sta = exeUpdate(cur,"insert into Person ('name','age') VALUES ('"+name+"',"+age+")")
    return render(request,'insert.html',{'status':sta})

#learn首页
def index(request):
    return render(request,'index.html')


#转换函数
def lindex(request):
    return HttpResponseRedirect(
        reverse('lhome')
    )

def p(request):
    return render(request,'post.html')

def posts(request):
    if request.method == 'POST':
        form = AddForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            print("================")
            print(name)
            print(password)
            return render(request,'index.html')


    else:
        form = AddForm()



    id = request.GET.get('id')

    print("++++++++++++++++++++++")
    print(id)
    return render(request,'post.html',{'form':form})


def lpost(request):
    return HttpResponseRedirect(
        reverse('lpost')
    )

#测试orm框架
def ormPerson(request):

    #db.connect()

    # 5. 创建表，这里有了safe=True选项，会在创建表之前先检查数据库里表是否已经存在,由于创建表的语句往往只需要使用一次，一般建议写入类或者方法中通过具体命令来调用
    # 注意：peewee里面创建表有两个方法， create_tables是`Database`中的方法，创建表时会建立表之间的关系和表的索引，使用`somedb.create_tables([Models], safe=False)`来调用
    # create_table是`Model`中的方法，仅仅创建表本身，而不包含索引和表之间的关系，使用`somemodel.create_table(safe=False)`来调用
    #db.create_table([Test],safe=True)
    #u = User.Select().where(User.username == 'wanglin').get()
    #print(u)
    u = User.get(User.username == "wanglin")
    #u = User.get(User.userage ==12 )
    print(u.__dict__)
    print("============================")
    for us in User.select():
        print(us.username)
    #db.close()
    return render(request,'ormPerson.html')

#测试返回json数据
def testJson(request):

    u1 = User()
    u1.username = 'wenyu'
    u1.userage = 12
    u1.userpawssword = '12'
    #u1.userdate = time.localtime()

    print("start=====================Object")
    print(u1)
    print("end===========================Object")

    print("start+++++++++++++++++++++++++++++++ObjectToJson")



    #u1Dict =  json.dumps(u1, default=convert_to_builtin_type)

    #u1json = json.dumps(u1Dict)

    #print(u1Dict)

    a = A()
    a.id = 1
    a.name = 'wanglin'
    a.pwd = 123

    jsonObject = json.dumps(a.__dict__);

    print(json.dumps(a.__dict__))

    print("end+++++++++++++++++++++++++++ObjectToJson")

    print("start=====================ObjectToJson")

    test = Test.select().dicts().get()
    print(test)

    print(json.dumps(str(test)))
    print("*********************")
    test = Test.select()
    print(test)

    print(json.dumps(str(test.__dict__)))


    print("end=====================ObjectToJson")



    u = User.select()

    print("++++++++++++++++++++++++++++++++++++++++")



    print("++++++++++++++++++++++++++++++++++++++++")

    return render(request,'ormPerson.html')

#ajax json
def ajaxJson(request):
    a = A()
    a.id = 1
    a.name = 'wanglin'
    a.pwd = 123

    id = request.POST['id']
    print("==========================")
    print(id)

    jsonObject = json.dumps(a.__dict__);
    response = JsonResponse(jsonObject, safe=False)
    response['Access-Control-Allow-Origin'] = '*'
    return response






def convert_to_builtin_type(obj):
    print ('default(', repr(obj), ')') # 把MyObj对象转换成dict类型的对象

    d = {  }

    d.update(obj.__dict__)

    return d