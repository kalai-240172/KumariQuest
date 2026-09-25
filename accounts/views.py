from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from planner.models import TripPlan
from tourism.models import Favorite
from .models import Profile

def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("home")

        return render(request, "login.html", {
            "error": "Invalid username or password."
        })

    return render(request, "login.html")


def register_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            return render(request, "register.html", {
                "error": "Passwords do not match."
            })

        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {
                "error": "Username already exists."
            })

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect("/login/")

    return render(request, "register.html")


def logout_view(request):
    logout(request)
    return redirect("/")

def profile_view(request):
    if not request.user.is_authenticated:
        return redirect("/login/")

    profile, created = Profile.objects.get_or_create(
        user=request.user
    )

    trips = TripPlan.objects.filter(
        user=request.user
    ).order_by("-created_at")

    favorites = Favorite.objects.filter(
        user=request.user
    ).select_related("destination")

    return render(request, "profile.html", {
        "profile": profile,
        "trips": trips,
        "favorites": favorites
    })

def edit_profile_view(request):
    if not request.user.is_authenticated:
        return redirect("/login/")

    profile, created = Profile.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":

        username = request.POST.get(
            "username",
            request.user.username
        ).strip()

        email = request.POST.get(
            "email",
            request.user.email
        ).strip()

        new_password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirm_password", "")

        # Check username
        if User.objects.exclude(
            pk=request.user.pk
        ).filter(username=username).exists():

            return render(request, "edit_profile.html", {
                "profile": profile,
                "error": "Username already exists."
            })

        # Check password
        if new_password:
            if new_password != confirm_password:
                return render(request, "edit_profile.html", {
                    "profile": profile,
                    "error": "Passwords do not match."
                })

            if len(new_password) < 8:
                return render(request, "edit_profile.html", {
                    "profile": profile,
                    "error": "Password must be at least 8 characters."
                })

            request.user.set_password(new_password)

        request.user.username = username
        request.user.email = email
        request.user.save()

        # Profile image
        if request.FILES.get("profile_image"):
            profile.profile_image = request.FILES["profile_image"]
            profile.save()

        # If password was changed, login again
        if new_password:
            login(request, request.user)

        return redirect("profile")

    return render(request, "edit_profile.html", {
        "profile": profile
    })