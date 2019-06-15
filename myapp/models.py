from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.name



class Notice(models.Model):

    name = models.TextField(max_length=4000,null=True, blank=True)
    message = models.TextField(max_length=4000, null=True, blank=True)
    topic = models.ForeignKey(Board, on_delete=models.CASCADE,null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return str(self.name) + str(self.message)

