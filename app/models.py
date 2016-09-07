from django.db import models

WYKLAD = 'WYK'
CWICZENIA = 'CW'
LABORATORIUM = 'LAB'
PROJEKT = 'PR'
SEMINARIUM = 'SEM'
CLASSES_CHOICES = (
    (WYKLAD, 'Wykład'),
    (CWICZENIA, 'Ćwiczenia'),
    (LABORATORIUM, 'Laboratorium'),
    (PROJEKT, 'Projekt'),
    (SEMINARIUM, 'Seminarium dyplomowe'),
)

LETNI = 'l'
ZIMOWY = 'z'
SEM_CHOICES = (
    (LETNI, 'letni'),
    (ZIMOWY, 'zimowy'),
)


class Semester(models.Model):
    name = models.CharField(max_length=8)
    sem_type = models.CharField(max_length=1, choices=SEM_CHOICES, default=ZIMOWY)
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=True)


class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)


class Group(models.Model):
    name = models.CharField(max_length=50)
    group_type = models.CharField(max_length=3, choices=CLASSES_CHOICES, default=WYKLAD)
    students = models.ManyToManyField(Student)


class Subject(models.Model):
    name = models.CharField(max_length=100)


class Classes(models.Model):
    class_type = models.CharField(max_length=3, choices=CLASSES_CHOICES, default=WYKLAD)
    subject = models.ForeignKey(Subject)
    group = models.ForeignKey(Group)