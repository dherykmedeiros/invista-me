from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import *
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def novo_usuario(request):
    if request.method == 'POST':
        formulario = UserRegisterForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            usuario = formulario.cleaned_data.get('username')
            messages.success(request, f'O usuario {usuario} foi criado com sucesso')
            return redirect('investimentos')
    
    else:
        formulario = UserRegisterForm()      
            
    return render(request,'usuarios/registrar.html', {'formulario': formulario})

@login_required
def logout_view(request):
    logout(request)
    return redirect('investimentos')