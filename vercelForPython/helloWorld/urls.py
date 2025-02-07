from . import views
from django.urls import path

app_name = "helloWorld"

urlpatterns = [
    path("", views.hello_world, name="hello"),
    path("post_blog/<str:name>", views.save, name="hello"),
    path("get_blog/<str:name>", views.get_blog, name="get_name"),
]