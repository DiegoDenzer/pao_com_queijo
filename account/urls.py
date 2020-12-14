from django.urls import path

from account.views import Register, cadastrar_usuario
from base.views import home_page

urlpatterns = [
    path('register', cadastrar_usuario, name='register'),
]
