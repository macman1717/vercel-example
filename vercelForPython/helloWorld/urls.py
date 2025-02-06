from vercelForPython.helloWorld import views
from django.urls import path

app_name = "hello"

urlpatterns = [
    path("", views.hello_world, name="hello"),
]