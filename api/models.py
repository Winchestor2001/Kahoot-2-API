from django.contrib.auth.models import User
from django.db import models


class GameQuiz(models.Model):
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    question = models.CharField()
    media = models.ImageField(null=True)
    game_token = models.ForeignKey('GroupSession', on_delete=models.CASCADE)
    variant_1 = models.CharField()
    variant_2 = models.CharField()
    variant_3 = models.CharField(null=True)
    variant_4 = models.CharField(null=True)
    answer = models.CharField(null=True)
    timer = models.IntegerField()
    score = models.IntegerField()

    def __str__(self):
        return self.game


class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField()

    def __str__(self):
        return self.title


class GroupSession(models.Model):
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    token = models.CharField()
    code = models.IntegerField()

    def __str__(self):
        return self.game


class Student(models.Model):
    nickname = models.CharField()
    avatar = models.CharField()
    score = models.IntegerField()
    game_token = models.ForeignKey(GroupSession, on_delete=models.CASCADE)

    def __str__(self):
        return self.nickname


class BioIcons(models.Model):
    image = models.ImageField(null=True, upload_to='icons/')

    def __str__(self):
        return self.image
