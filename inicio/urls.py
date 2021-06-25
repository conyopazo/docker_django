from django.urls import path
from. import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('entrevistador', views.entrevistador, name="entrevistador"),
    path('add_venue/', views.add_venue, name="add-venue"),
		path('agenda/', views.agenda, name="agenda"),
		path('miusuario/', views.miUsuario, name="miUsuario"),
		path('videollamada/', views.videollamada, name="videollamada"),
    ]