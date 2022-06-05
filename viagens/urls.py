from django.urls import path

from . import views

app_name = "viagens"

urlpatterns = [
    path('', views.viagens, name="viagens"),
    path('create_viagens/', views.create_viagens, name="create_viagens"),
]
