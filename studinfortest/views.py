# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import *
from django.http import HttpResponse


# Create your views here.
def index_view(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        #接收请示参数
        sname = request.POST.get('sname', '')
        cname = request.POST.get('clsname', '')
        coursenames = request.POST.getlist('coursename', [])

        #将数据注册到数据库
        flag = registerStu(sname, cname, *coursenames)
        if flag:
            return HttpResponse('注册成功！')

        return HttpResponse('注册失败！')

#显示所有班级信息
def showall_view(request):
    cls = Clazz.objects.all()

    return render(request, 'showall.html', {'cls': cls})

    #查询班级表中的所有数据

#显示当前班级下的所有学生信息
def getstu_view(request):
    #获取班级编号
    cno = request.GET.get('cno', '')
    no = int(cno)

    #根据班级编号查询学生信息

    stus = Clazz.objects.get(cno=no).student_set.all()
    return render(request, 'stulist.html', {'stus': stus})