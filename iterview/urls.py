from django.urls import path, include
from. import views

#rutas para la URL (ejemplo: "pepo.cl/inicio")

urlpatterns = [
    path('', views.inicio, name="inicio"),
		path('register_postulante/', views.register_request_2, name="register_postulante"),
		path('register_entrevistador/', views.register_request, name="register_entrevistador"),
		path('signin/',views.signin,name="login"),
		path('signin_postulante/',views.login_request_2,name="login_postulante"),
		path('signin_entrevistador/', views.login_request, name="login_entrevistador"),
		path('logout/', views.logout_request, name="logout"),
		path('videollamada/', views.videollamada, name="videollamada"),
		path('agenda/', views.agenda, name="agenda"),
		path('delete_agenda/<str:pk>/', views.deleteAgenda, name="delete_agenda"),
		path('update_agenda/<str:pk>/', views.updateAgenda, name="update_agenda"),
		path('miusuario/', views.miUsuario, name="miUsuario"),
    path("miusuario_entrevistador/", views.miUsuarioEntrevistador, name="miUsuarioEntrevistador"),
    path("ambienteprogramacion/", views.ambienteProgramacion, name="ambienteProgramacion"),
    path("ambientepizarra/", views.ambientePizarra, name="ambientePizarra"),
    ]
