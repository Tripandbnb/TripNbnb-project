from django.urls import path
from . import views

app_name = "reservations"

urlpatterns = [
    path("place/check/", views.reservation_check, name = "select"),
    path("place/create/", views.reservation_confirm, name = "create"),
    path("delete/<int:id>/", views.reservation_cancel, name = "delete")
]
