from django.contrib import admin
from .models import *


@admin.register(GameQuiz)
class GameQuizAdmin(admin.ModelAdmin):
    list_display = ['game', 'timer', 'score']


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['user', 'title']


@admin.register(GroupSession)
class GroupSessionAdmin(admin.ModelAdmin):
    list_display = ['game', 'code']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['nickname', 'score']


@admin.register(BioIcons)
class BioIconsAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']
