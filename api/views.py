from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from .models import *
from .serializers import *
from rest_framework import generics

from .utils import get_user_from_token


class HomeView(APIView):
    def get(self, request):
        return Response({}, status=200)


class UserGameAPI(APIView):
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        user_id = get_user_from_token(request.auth.key)
        games = Game.objects.filter(user=user_id)
        serializer = GameSerializer(data=games, many=True)
        serializer.is_valid()
        return Response(serializer.data, status=200)

    def post(self, request):
        user = User.objects.get(id=get_user_from_token(request.auth.key))
        title = request.data.get('title')
        questions = request.data.get('questions')
        game = Game.objects.create(user=user, title=title)
        for q in questions:
            GameQuiz.objects.create(
                game=game, question=q['question'],
                variant_1=q['variant_1'], variant_2=q['variant_2'],
                variant_3=q['variant_3'], variant_4=q['variant_4'],
                answer=q['answer'], timer=q['timer'], score=q['score']
            )

        return Response({"STATUS": "CREATED"}, status=201)
