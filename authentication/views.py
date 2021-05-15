import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, generics, status, response, parsers, decorators
from rest_framework.generics import ListAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from authentication.models import UserModel
from authentication.serializers import UserSerializer, RegisterSerializer, MyTokenObtainPairSerializer, \
    UserImageSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    @decorators.action(
        detail=True,
        methods=['GET','PUT'],
        serializer_class=UserImageSerializer,
        parser_classes=[parsers.MultiPartParser],
    )
    def resim(self, request, pk):
        obj = self.get_object()
        serializer = self.serializer_class(obj, data=request.data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors,
                                 status.HTTP_400_BAD_REQUEST)


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    #permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
