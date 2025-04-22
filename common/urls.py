from django.urls import path
from common import views

app_name = "common"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("about/", views.AboutView.as_view(), name = "about"),
]

