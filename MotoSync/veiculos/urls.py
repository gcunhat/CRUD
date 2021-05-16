from django.urls import path

from . import views

urlpatterns = [
    path('inicio/',views.inicio),
    path('veiculosCad/',views.veiculosCad, name="veiculosCad"),
    path('yourname/<str:name>', views.yourName, name="your-name" )
]