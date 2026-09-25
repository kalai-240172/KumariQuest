"""
URL configuration for kumariquest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import login_view

from tourism.views import home, destination_detail, explore_destinations


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", login_view, name="login_home"),
    path("home/", home, name="home"),
    path(
        "destination/<int:pk>/",
        destination_detail,
        name="destination_detail"
    ),
    path("explore/", explore_destinations, name="explore"),
    path("planner/", include("planner.urls")),
    path(
    "",
    include("tourism.urls")
),
    path("login/", include("accounts.urls")),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
