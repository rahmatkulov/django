from django.urls import path
from common.views import home, about,contact


app_name = "common"

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name = "about"),
    path("contact/", contact, name = "contact")
]

