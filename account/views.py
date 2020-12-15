from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def cadastrar_usuario(request):
    template_name = 'account/register.html'

    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('login')
    else:
        form_usuario = UserCreationForm()
    return render(request, template_name, {'form': form_usuario})
