from django.contrib.auth.models import User
from django.db import models


class GameQuiz(models.Model):
    question_num = models.IntegerField(default=0)
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    media = models.ImageField(null=True, upload_to='quiz_media/', blank=True)
    variant_1 = models.CharField(max_length=255)
    variant_2 = models.CharField(max_length=255)
    variant_3 = models.CharField(max_length=255, null=True)
    variant_4 = models.CharField(max_length=255, null=True)
    answer = models.CharField(max_length=255, null=True)
    timer = models.IntegerField()
    score = models.IntegerField()

    def __str__(self):
        return self.game.title

    class Meta:
        ordering = ['question_num']


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
    avatar = models.ForeignKey("BioIcons", on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    token = models.CharField(max_length=255, blank=True, null=True)
    game = models.ForeignKey("Game", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nickname


class BioIcons(models.Model):
    image = models.ImageField(null=True, upload_to='icons/')

