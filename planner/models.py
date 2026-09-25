from django.db import models
from django.contrib.auth.models import User


class TripPlan(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    days = models.IntegerField()

    category = models.CharField(
        max_length=100
    )

    trip_type = models.CharField(
        max_length=50
    )

    budget = models.CharField(
        max_length=50
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.days} Day Trip"