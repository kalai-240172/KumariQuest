from django.db import models
from django.contrib.auth.models import User


class Destination(models.Model):

    name = models.CharField(max_length=200)

    category = models.CharField(max_length=100)

    description = models.TextField()

    location = models.CharField(max_length=200)

    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )

    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )

    visiting_hours = models.CharField(max_length=100)

    best_time = models.CharField(max_length=100)

    entry_fee = models.CharField(
        max_length=100,
        default="Free"
    )

    budget_level = models.CharField(
        max_length=50,
        default="Budget"
    )

    image = models.ImageField(
        upload_to="destinations/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class Favorite(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        unique_together = ("user", "destination")

    def __str__(self):
        return f"{self.user.username} - {self.destination.name}"

class Notification(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    title = models.CharField(
        max_length=200
    )

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    is_read = models.BooleanField(
        default=False
    )

    def __str__(self):
        return f"{self.user.username} - {self.title}"

class Review(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    rating = models.IntegerField()

    comment = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username} - KumariQuest"