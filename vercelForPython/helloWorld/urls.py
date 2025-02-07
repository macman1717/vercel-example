from . import views
from django.urls import path

app_name = "helloWorld"

urlpatterns = [
    path("", views.hello_world, name="hello"),
]