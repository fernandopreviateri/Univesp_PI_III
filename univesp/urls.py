"""univesp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from app import views
from django.contrib import admin
from django.urls import path



urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', views.logon, name="logon"),
    path('login', views.loginUser, name="login"),
    path('index/', views.index, name="index"),
    path('cadastro/', views.cadastro, name="cadastro"),
    path('lista/', views.lista, name="lista"),
    path('questionario/', views.questionario, name="questionario"),
    #path('questionario/<slug:paciente_id', views.questionario, name="questionario"),
    
]
