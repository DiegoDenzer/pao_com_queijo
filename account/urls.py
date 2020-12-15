from django.urls import path

from account.views import cadastrar_usuario

urlpatterns = [
    path('register', cadastrar_usuario, name='register'),
]
