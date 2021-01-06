# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
from django.db.models import Manager


class Clazz(models.Model):
    cno = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=30)

    def __str__(self):
        return u'Clazz:%s' % self.cname

class Course(models.Model):
    course_no = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=30)

    def __str__(self):
        return u'Course:%s' % self.course_name

# Student.objects.create
class CustomManager(Manager):

    #班级表入库,返回一个班级对象
    def getClsobj(self, cname):
        try:
            cls = Clazz.objects.get(cname=cname)
        except Clazz.DoesNotExist:
            cls = Clazz.objects.create(cname=cname)
        return cls

    def create(self, **kwargs):
        clazz = kwargs.get('clazz', '')
        clas = self.getClsobj(clazz)


# Student.objects.create(sname='lisi',clazz='B2004Python',course=('HTML5','UI', 'JAVA' ,'Python'))
class Student(models.Model):
    sno = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=30)
    cls = models.ForeignKey(Clazz, on_delete=models.SET_DEFAULT, default='默认值')
    cour = models.ManyToManyField(Course)

    objects = CustomManager()

    def __str__(self):
        return u'Student:%s' % self.sname


#根据班级名称获取班级对象
def getCls(cname):
    try:
        cls = Clazz.objects.get(cname=cname)
    except Clazz.DoesNotExist:
        cls = Clazz.objects.create(cname=cname)
    return cls

#获取课程对象列表
def getCourseList(*coursenames):
    courseList = []

    for cn in coursenames:
        try:
            c = Course.objects.get(course_name=cn)
        except Course.DoesNotExist:
            c = Course.objects.create(course_name=cn)
        courseList.append(c)
    return courseList


def registerStu(sname, cname, *coursenames):
    #1.获取班级对象
    cls = getCls(cname)
    #2.获取课程对象列表
    courseList = getCourseList(*coursenames)
    #3.插入学生表数据
    try:
        stu = Student.objects.get(sname=sname)
    except Student.DoesNotExist:
        stu = Student.objects.create(sname=sname, cls=cls)
    #4.插入中间表数据
    stu.cour.add(*courseList)

    return True


