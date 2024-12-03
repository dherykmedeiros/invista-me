"""
URL configuration for projeto_invista_me project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from invista_me.views import * 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', investimentos, name='investimentos'),
    path('novo_investimento/', criar, name='novo_investimento'),
    path('/<int:id_investimento>',detalhe, name='detalhe'),
    path('novo_investimento/<int:id_investimento>',editar, name='editar'),
    path('excluir_investimento/<int:id_investimento>', excluir, name='excluir')
    
]
