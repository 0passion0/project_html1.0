import re
import requests
import lxml
from lxml import etree
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from openpyxl import load_workbook
from pandas import read_csv
from django.shortcuts import render
import hashlib
headers_list = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
}


def newinter(request):
    if request.session.keys():
        data = []
        u = "http://news.china.com.cn/world/node_7184857.htm"
        res = requests.get(u, headers=headers_list)
        res.encoding = 'utf-8'
        html = etree.HTML(res.text)
        tab = html.xpath("/html/body/div[4]/div[1]/div[2]/div")
        for i in tab:
            x = i.xpath('./div[1]/h2/a/text()')
            p = (i.xpath('./div[1]/h2/a/@href'))
            data.append({"table": x, "url": p})
        return render(request, 'newinter.html', {"data": data})
    else:
        return redirect("/denglu/")

def deng(request,str):
    if request.session.keys():
        return render(request, str)
    else:
        return redirect("/denglu/")
def newchine(request):
    if request.session.keys():
        data = []
        u = "http://news.china.com.cn/node_7247302.htm"
        res = requests.get(u, headers=headers_list)
        res.encoding = 'utf-8'
        html = etree.HTML(res.text)
        tab = html.xpath("/html/body/div[4]/div[1]/div[2]/div")
        for i in tab:
            x = i.xpath('./div[1]/h2/a/text()')
            p = (i.xpath('./div[1]/h2/a/@href'))
            data.append({"table": x, "url": p})
        return render(request, 'newwor.html', {"data": data})
    else:
        return redirect("/denglu/")

def newwor(request):
    if request.session.keys():
        data = []
        u = "http://military.china.com.cn/"
        res = requests.get(u, headers=headers_list)
        res.encoding = 'utf-8'
        html = etree.HTML(res.text)
        tab = html.xpath("/html/body/div[4]/div[1]/div[2]/div")
        for i in tab:
            x = i.xpath('./div[1]/h2/a/text()')
            p = (i.xpath('./div[1]/h2/a/@href'))
            data.append({"table": x, "url": p})
        return render(request, 'newchine.html', {"data": data})
    else:
        return redirect("/denglu/")
def newso(request):
    if request.session.keys():
        data = []
        u = "http://shehui.china.com.cn/node_7247305.htm"
        res = requests.get(u, headers=headers_list)
        res.encoding = 'utf-8'
        html = etree.HTML(res.text)
        tab = html.xpath("/html/body/div[4]/div[1]/div[2]/div")
        for i in tab:
            x = i.xpath('./div[1]/h2/a/text()')
            p = (i.xpath('./div[1]/h2/a/@href'))
            data.append({"table": x, "url": p})
        return render(request, 'newso.html', {"data": data})
    else:
        return redirect("/denglu/")
