# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth import User
from django import timestamp

from .models import *

# Register your models here.
class Post(models.Model):
    name = models.CharField(max_length=200, blank=False)
    description = models.CharField(max_length=400)
    price = models.FloatField(max_digits=100, blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id

class User(models.Model):
    freelancer = models.OneToOneField(Freelancer,)
    client = models.OneToOneField()        

class Client(models.Model):
    name = models.CharField(User, blank=False)
    job = models.OneToOneField(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Freelancer(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(blank=False)
    email = models.EmailField(blank=False)

    def __str__(self):
        return self.name

