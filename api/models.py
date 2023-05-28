from django.contrib.auth.models import User
from django.db import models


class GameQuiz(models.Model):
    user = models.CharField()
    question = models.CharField()
    media = models.ImageField(null=True)
    game_token = models.CharField()
    token = models.CharField()
    variant_1 = models.CharField()
    variant_2 = models.CharField()
    variant_3 = models.CharField(null=True)
    variant_4 = models.CharField(null=True)
    timer = models.TimeField()
    score = models.IntegerField()


class Game(models.Model):
    user = models.CharField()
    title = models.CharField()


class GroupSession(models.Model):
    game = models.CharField()
    token = models.CharField()
    code = models.IntegerField()


class Student(models.Model):
    nickname = models.CharField()
    avatar = models.CharField()
    score = models.IntegerField()
    game_token = models.CharField()


class BioIcons(models.Model):
    image = models.ImageField(null=True)