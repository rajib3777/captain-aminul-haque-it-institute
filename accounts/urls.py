from django.urls import path
from .views import register, health

urlpatterns = [
    path("api/register/", register),
    path("health/", health),
]
