from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render
from users import models as users_model

# Create your views here.
def HomeView(request):
    return render(request, "base.html")