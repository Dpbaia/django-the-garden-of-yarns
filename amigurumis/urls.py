from django.urls import path

from . import views

app_name = "amigurumis"
urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("socials/", views.socials, name="socials"),
    path("<int:pk>/", views.detail, name="amigurumi-detail"),
    path("<str:authorship>/", views.list, name="list"),
]
