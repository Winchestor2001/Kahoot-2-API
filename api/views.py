from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from rest_framework import generics


class HomeView(APIView):
    def get(self, request):
        return Response({}, status=200)
