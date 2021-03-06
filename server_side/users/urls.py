from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login/", views.kakao_login, name="login"),
    path("unlink/", views.kakao_unlink, name="unlink"),
    path("<int:pk>", views.get_profile, name="proflile"),
]