from django.contrib import admin
from .models import Destination
from .models import Destination, Favorite, Notification,Review


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "category",
        "location",
        "entry_fee",
        "budget_level",
    )

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "title",
        "is_read",
        "created_at",
    )

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "rating",
        "comment",
        "created_at",
    )