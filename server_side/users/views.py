import os
import requests
import json
from django.shortcuts import reverse, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.core.files.base import ContentFile
from . import forms, models
from rest_framework import viewsets  # add this
from .serializers import UserSerializer  # add this


# Create your views here.
class UserView(viewsets.ModelViewSet):  # add this
    serializer_class = UserSerializer  # add this
    queryset = models.User.objects.all()
    print()


@method_decorator(csrf_exempt, name="dispatch")
def kakao_login(request):
    received_json_data = json.loads(request.body.decode("utf-8"))
    pk = received_json_data.get("id")
    properties = received_json_data.get("properties")
    nickname = properties.get("nickname")
    profile_image = properties.get("profile_image")
    try:
        user = models.User.objects.get(pk=pk)
    except models.User.DoesNotExist:
        print("Not found")
        user = models.User.objects.create(
            pk=pk,
            username=nickname,
            first_name=nickname,
        )
        user.set_unusable_password()
        user.save()
        if profile_image is not None:
            photo_request = requests.get(profile_image)
            user.profile_img.save(
                f"{nickname}-profile image", ContentFile(photo_request.content)
            )
    login(request, user)
    return redirect("http://localhost:3000")


def log_out(request):
    logout(request)
    return redirect("https://localhost:3000")
