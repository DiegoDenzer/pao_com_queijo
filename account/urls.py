from django.urls import path

from account.views import Register, cadastrar_usuario
from base.views import home_page

urlpatterns = [
    # path('register', Register.as_view(), name='register'),
    path('register2', cadastrar_usuario, name='register'),
]