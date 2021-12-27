from django.urls import path

from . import views

app_name = "amigurumis"
urlpatterns = [
    
    path('', views.index, name='index'),
]