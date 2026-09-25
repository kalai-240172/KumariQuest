from django.contrib import admin
from .models import TripPlan


@admin.register(TripPlan)
class TripPlanAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "days",
        "category",
        "trip_type",
        "budget",
        "created_at",
    )