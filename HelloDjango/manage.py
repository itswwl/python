#!/usr/bin/env python
import os
import sys

"""
python3 教程 ： http://www.runoob.com/python3/python3-dictionary.html

Django 基础教程 ： http://www.ziqiangxuetang.com/django/django-models.html

在PyCharm下搭建开发环境 ：
http://jingyan.baidu.com/article/fdffd1f85fa64ff3e98ca1a8.html

用pycharm+django开发web项目 运行项目 ：
 http://blog.csdn.net/ll1058320115/article/details/50389067


 链接数据库操作
 Python3.5连接Mysql ： http://www.cnblogs.com/rusking/p/5090395.html

 windows系统下，django1.8+python3.5使用pymysql链接 mysql数据库 ：
 http://blog.csdn.net/rao356/article/details/48975617

 python模块pymysql :
 http://blog.itpub.net/29974949/viewspace-1562574/
"""

"""



完成页面的遍历输出                       解决



完成简单的增删该查


实体与sql查询对应      实际是Orm框架映射

    from django.db import models 和from peewee import *  会冲突

    (1):python ORM 模块peewee(一): 建立数据库对象
        http://www.cnblogs.com/noway-neway/p/5272688.html
    (2):python ORM 模块peewee(二): 数据库使用的基本流程
        http://www.cnblogs.com/noway-neway/p/5274814.html
    (3):python ORM 模块peewee(三): Model的建立
        http://www.cnblogs.com/noway-neway/p/5275138.html


    (1):Python的ORM框架Peewee使用入门(一)
        http://blog.csdn.net/WuLex/article/details/52565681
    (2):Python的ORM框架Peewee使用入门(二)
        http://blog.csdn.net/wulex/article/details/52566990
    (3):Python的ORM框架Peewee使用入门(三)
        http://blog.csdn.net/wulex/article/details/52567082



怎样将查询到的结果转成实体或者字典
对象.__dict__


解决peewee 转json问题
http://stackoverflow.com/questions/21975920/peewee-model-to-json

返回json数据
http://www.ziqiangxuetang.com/django/django-ajax.html


详解Python中的序列化与反序列化的使用
http://www.jb51.net/article/68667.htm


获取时间
python 的常用时间操作，取得当前时间等
http://blog.csdn.net/caisini_vc/article/details/5619954



py引用py
http://zhidao.baidu.com/question/1797701025194549987.html




添加JQuery，使用JQuery Ajax完成请求()         完成删除
http://www.cnblogs.com/fnng/p/3565912.html
http://www.cnblogs.com/qq78292959/p/3238739.html

post 表单 提交
http://www.ziqiangxuetang.com/django/django-forms.html


不同页面的跳转       解决
http://www.ziqiangxuetang.com/django/django-url-name.html



怎样断点调试
http://blog.csdn.net/chenggong2dm/article/details/9368641
http://www.68idc.cn/help/buildlang/ask/20151211595596.html

怎样引入静态文件   解决
http://blog.csdn.net/zp919191/article/details/50412402
"""

"""
常见问题
(一)：django提交表单提示"You called this URL via POST, but the URL doesn't end in a slash and you have APPEND_SL
http://blog.csdn.net/krista2009/article/details/43337373

(二)：In order to allow non-dict objects to be serialized set the safe parameter to False.
Django开发博客（十一）—跨域资源共享（CORS）
http://blog.csdn.net/wyb199026/article/details/51598765

"""

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HelloDjango.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
