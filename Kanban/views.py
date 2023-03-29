from turtle import color, title
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User
from Kanban.script import check_for_mail, check_for_user
from rest_framework import viewsets, status
from Kanban.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from rest_framework.settings import api_settings
# from django.dispatch import receiver
from rest_framework.authentication import TokenAuthentication
# from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from .models import Contact, Task, category, subtask
from .serializers import CategorySerializer, ContactSerializer, SubtaskSerializer, TaskSerializer
import json
from django.core import serializers
from datetime import datetime


# @receiver(post_save, sender=User)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)


@csrf_exempt
@require_http_methods(["POST"])
def register_view(request):
    if check_for_user(request) and check_for_mail(request):
        User.objects.create_user(username=request.POST.get('userName', None),
                                 email=request.POST.get(
            'email', None),
            password=request.POST.get('password', None), first_name=request.POST.get('userName', None))
        return HttpResponse(status=200)
    else:
        return HttpResponse({'error2': 'user aready exists'})


class login_View(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        })


class TaskViewset(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    queryset = category.objects.all()
    serializer_class = CategorySerializer


class ContactViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SubTaskViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    queryset = subtask.objects.all()
    serializer_class = SubtaskSerializer
