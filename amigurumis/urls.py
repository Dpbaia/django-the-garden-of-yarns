from django.urls import path

from . import views

app_name = "amigurumis"
urlpatterns = [
    
    path('', views.index, name='index'),

    # !
    path('<str:authorship>/', views.list, name='list'),
    # path('ownrecipe', views.allworks, name='allworks'),

]