import random
from uuid import uuid4

from django.http import StreamingHttpResponse
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
        print(games)
        serializer = GameSerializer(instance=games, many=True)
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


class GroupSessionAPI(APIView):

    def get(self, request):
        game = Game.objects.get(id=request.data.get("game_id"))
        rand_token = uuid4()
        code = random.randint(10000, 999999)
        game_session = GroupSession.objects.create(
            game=game, token=rand_token, code=code
        )
        serializer = GroupSessionSerializer(instance=game_session)
        return Response(serializer.data, status=200)


class StudentSessionAPI(APIView):
    def get(self, request):
        game_code = request.data.get("code")
        game = GroupSession.objects.get(code=game_code)
        icons = BioIcons.objects.all()
        serializer = BioIconsSerializer(instance=icons, many=True)
        return Response({"game_token": game.token, "icons": serializer.data}, status=200)

    def post(self, request):
        game_token = Game.objects.get(id=GroupSession.objects.get(token=request.data.get("game_token")).game.id)
        nickname = request.data.get("nickname")
        avatar = BioIcons.objects.get(id=request.data.get("avatar"))
        token = uuid4()
        student = Student.objects.create(
            nickname=nickname, avatar=avatar, token=token, game=game_token
        )
        return Response({"student_token": student.token}, status=200)


class StartGameSessionAPI(APIView):
    def get(self, request):
        game_token = request.data.get("game_token")
        game = GroupSession.objects.get(token=game_token)
        question = GameQuiz.objects.filter(game=game.game.id)
        serializer = GameQuizSerializer(instance=question[0])
        return Response(serializer.data, status=200)

