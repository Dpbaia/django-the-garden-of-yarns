from django.urls import path

from . import views

app_name = "amigurumis"
urlpatterns = [
    # Remember: Order is important!
    
    path('', views.index, name='index'),

    # CREATING A GENERIC VIEW:
    # path('<str:authorship>/', views.AmigurumiListView.as_view(), name='list'),

    # !
    path('<str:authorship>/', views.list, name='list'),


]