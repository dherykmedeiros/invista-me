from django.contrib import admin
from django.urls import path
from invista_me.views import * 
from usuarios.views import * 
from django.contrib.auth import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', investimentos, name='investimentos'),
    path('novo_investimento/', criar, name='novo_investimento'),
    path('/<int:id_investimento>',detalhe, name='detalhe'),
    path('novo_investimento/<int:id_investimento>',editar, name='editar'),
    path('excluir_investimento/<int:id_investimento>', excluir, name='excluir'),
    path('conta/', novo_usuario, name='novo_usuario'),
    path('login/',views.LoginView.as_view(template_name = 'usuarios/login.html'), name='login'),
    path('logout/',logout_view, name='logout'),
    
]
