from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
# Create your models here.


# class User(models.Model):
#     name = models.CharField(max_length=60)
#     email = models.CharField(max_length=60, unique=True)
#     password = models.CharField(max_length=60)

#     def __str__(self):
#         return self.name


class Question(models.Model):
    title = models.CharField(max_length=500)
    content = models.CharField(max_length=5000)
    user = models.ForeignKey(User)
    updatedate = models.DateTimeField(default=datetime.now, blank=True)
