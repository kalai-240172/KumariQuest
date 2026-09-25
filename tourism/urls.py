from django.urls import path
from .views import (
    notifications,
    mark_notification_read,
    feedback_view,
    safety_tips,
    about
)

urlpatterns = [
    path(
        "notifications/",
        notifications,
        name="notifications"
    ),

    path(
        "notifications/read/<int:pk>/",
        mark_notification_read,
        name="mark_notification_read"
    ),
    path("feedback/", feedback_view, name="feedback"),
    path("safety/", safety_tips, name="safety"),
    path("about/", about, name="about"),

    
]