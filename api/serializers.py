from rest_framework import serializers
from .models import *


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


class GroupSessionSerializer(serializers.ModelSerializer):
    game = GameSerializer()

    class Meta:
        model = GroupSession
        fields = '__all__'


class GameQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameQuiz
        fields = '__all__'


class BioIconsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BioIcons
        fields = '__all__'
