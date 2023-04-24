from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from openpyxl import load_workbook
from pandas import read_csv
from django.shortcuts import render
import hashlib

def setPassword(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    result = md5.hexdigest()
    return result

# Create your views here.
from app import models

def denglu(request):
    return render(request, "denglu.html")
def admin(request):
    print(request.session)
    if request.session.keys():
        return render(request, "admin.html")
    else:
        return redirect("/denglu/")

def banji(request):
    if request.session.keys():
        pus = models.Userment.objects.all()
        return render(request, "banji.html", {"data": pus})
    else:
        return redirect("/denglu/")
def student_add(request):
    if request.session.keys():
        if request.method == "GET":
            return render(request, "student_add.html")
        else:
            id = request.POST.get("id")
            name = request.POST.get("name")
            gender = request.POST.get("gender")
            math = request.POST.get("math")
            python = request.POST.get("python")
            C = request.POST.get("C")
            coun = math + python + C
            models.Userment.objects.create(id=id, name=name, gender=gender, math=math, python=python, C=C, coun=coun)
            return redirect("/admin/")
    else:
        return redirect("/denglu/")



def student_cha(request):
    if request.session.keys():
        if request.method == "GET":
            return render(request, "student_cha.html")
        else:
            id = request.POST.get("id")
            name = request.POST.get("name")
            gender = request.POST.get("gender")
            math = request.POST.get("math")
            python = request.POST.get("python")
            C = request.POST.get("C")
            coun = math + python + C
            models.Userment.objects.filter(id=id).update(name=name, gender=gender, math=math, python=python, C=C,
                                                         coun=coun)
            return redirect("/admin/")
    else:
        return redirect("/denglu/")

def student_dele(request):
    if request.session.keys():
        if request.method == "GET":
            return render(request, "student_dele.html")
        else:
            id = request.POST.get('id')
            print(id)
            models.Userment.objects.filter(id=id).delete()
            return redirect("/admin/")
    else:
        return redirect("/denglu/")

def deng(request,str):
    if request.session.keys():
        return render(request, str)
    else:
        return redirect("/denglu/")
def gushi1(request):
    return deng(request, "gushi1.html")

def gushi2(request):
    return deng(request, "gushi2.html")


def gushi3(request):
    return deng(request, "gushi3.html")


def gushi4(request):
    return deng(request, "gushi4.html")


"""传输照片"""


def phon(request):
    if request.session.keys():
        if request.method == "GET":
            return render(request, 'phone.html')

        print(request.POST)
        file_object = request.FILES.get("tlg")
        print(file_object)
        name = file_object.name
        f = open("app/static/app/" + name, mode='wb')
        for i in file_object.chunks():
            f.write(i)
        return redirect("/admin/")
    else:
        return redirect("/denglu/")


"""调查表"""
def diaocha(request):
    if request.session.keys():
        if request.method == "GET":
            return render(request, "调查.html")
        else:

            q1_1 = request.POST.get("q1_1")
            q1_2 = request.POST.get("q1_2")
            q1_3 = request.POST.get("q1_3")

            # 问题 2
            q2_1 = request.POST.get("q2_1")
            q2_2 = request.POST.get("q2_2")
            q2_3 = request.POST.get("q2_3")
            q2_4 = request.POST.get("q2_4")

            # 问题 3
            q3_1 = request.POST.get("q3_1")
            q3_2 = request.POST.get("q3_2")
            q3_3 = request.POST.get("q3_3")
            q3_4 = request.POST.get("q3_4[]")
            q3_5 = request.POST.get("q3_5[]")

            # 问题 4
            q4_1 = request.POST.get("q4_1")
            q4_2 = request.POST.get("q4_2")
            q4_3 = request.POST.get("q4_3[]")
            q4_4 = request.POST.get("q4_4")
            q4_5 = request.POST.get("q4_5[]")

            print(q1_1)
            models.Survey.objects.create(q1_1=q1_1, q1_2=q1_2, q1_3=q1_3,
                                         q2_1=q2_1, q2_2=q2_2, q2_3=q2_3, q2_4=q2_4,
                                         q3_1=q3_1, q3_2=q3_2, q3_3=q3_3, q3_4=q3_4, q3_5=q3_5,
                                         q4_1=q4_1, q4_2=q4_2, q4_3=q4_3, q4_4=q4_4, q4_5=q4_5
                                         )
            return redirect("/admin/")
    else:
        return redirect("/denglu/")


import hashlib

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


class LoginFrom(forms.Form):
    username=forms.CharField(label="用户名",widget=forms.TextInput,required=True)
    password = forms.CharField(label="密码",widget=forms.PasswordInput(render_value=True),required=True)
    def clean_password(self):
        pwd=self.cleaned_data.get("password")
        m = hashlib.md5()
        m.update(pwd.encode("utf8"))
        mpwd = m.hexdigest()
        return mpwd

def login_view(request):
    form=LoginFrom()
    if request.method == 'POST':
        form=LoginFrom(data=request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            ter=models.User.objects.filter(username=form.cleaned_data["username"],password=form.cleaned_data["password"]).first()
            if not ter:
                form.add_error("password","用户名或密码错误")
                return render(request, 'denglu.html', {'form': form})
            request.session["info"]= {'id':ter.id,'name':ter.username}
            return redirect("/admin/")
    else:
        return render(request, 'denglu.html',{'form':form})
def xiaren(request):
    return  redirect("/static/app/6_210702183620_1.jpg")


