"""HelloDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import import_module,include,url


from django.conf.urls import url
from django.contrib import admin
from hello import views as h
from learn import views as l
from HelloDjango import settings
"""
url(r'^index/$',hello.views.hello),
    url(r'^admin/', admin.site.urls),
"""
"""
   url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': settings.STATIC_ROOT }),
"""



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', h.hello),
    url(r'^home/$', l.home , name='lhome'),
    url(r'^home/$', l.home ),
    url(r'^delete', l.delete, name='delete'),
    url(r'^lindex/$', l.index),
    url(r'^p/$', l.p),
    url(r'^lpost/$', l.posts,name="lpost"),
    url(r'^ormPerson/$', l.ormPerson),
    url(r'^testJson/$', l.testJson),
    url(r'^ajaxJson/$', l.ajaxJson),
    #url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': settings.STATIC_ROOT}),

]

