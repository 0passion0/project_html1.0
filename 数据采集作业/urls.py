"""数据采集作业 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import app.views
import app.cachong

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('admin/', app.views.admin),
    path('banji/', app.views.banji),
    path('student/add/', app.views.student_add),
    path('student/cha/', app.views.student_cha),
    path('student/dele/', app.views.student_dele),
    path('denglu/', app.views.login_view),
    path('gushi1/', app.views.gushi1),
    path('gushi2/', app.views.gushi2),
    path('gushi3/', app.views.gushi3),
    path('gushi4/', app.views.gushi4),
    path('phone/', app.views.phon),
    path('调查/', app.views.diaocha),
    path('newinter/', app.cachong.newinter),
    path('newchine/', app.cachong.newchine),
    path('newwor/', app.cachong.newwor),
    path('newso/', app.cachong.newso),
    path('xiaren/', app.views.xiaren)
]
