from django.urls import path
from . import views
 
urlpatterns = [
    path("", views.index, name="index"),
    path("sobre/", views.sobre, name="sobre"),
    path("ola/<str:nome>/", views.saudacao, name="saudacao"),
    path("dobro/<int:numero>/", views.dobro, name="dobro"),
    path("tabuada/<int:n>/", views.tabuada, name="tabuada"),
    path("perfil/<str:nome>/<int:idade>/", views.perfil, name="perfil"),

]
