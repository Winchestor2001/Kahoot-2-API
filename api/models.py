from django.contrib.auth.models import User
from django.db import models


class GameQuiz(models.Model):
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    media = models.ImageField(null=True, upload_to='quiz_media/', blank=True)
    game_token = models.ForeignKey('GroupSession', on_delete=models.CASCADE, null=True, blank=True)
    variant_1 = models.CharField(max_length=255)
    variant_2 = models.CharField(max_length=255)
    variant_3 = models.CharField(max_length=255, null=True)
    variant_4 = models.CharField(max_length=255, null=True)
    answer = models.CharField(max_length=255, null=True)
    timer = models.IntegerField()
    score = models.IntegerField()

    def __str__(self):
        return self.game.title


class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class GroupSession(models.Model):
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    token = models.CharField(max_length=255)
    code = models.IntegerField(default=0)

    def __str__(self):
        return self.game.title


class Student(models.Model):
    nickname = models.CharField(max_length=255)
    avatar = models.CharField(max_length=255)
    score = models.IntegerField()
    game_token = models.ForeignKey(GroupSession, on_delete=models.CASCADE)

    def __str__(self):
        return self.nickname


class BioIcons(models.Model):
    image = models.ImageField(null=True, upload_to='icons/')

    def __str__(self):
        return self.image
