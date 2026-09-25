from django.urls import path
from .views import planner_home

urlpatterns = [
    path("", planner_home, name="planner"),
]