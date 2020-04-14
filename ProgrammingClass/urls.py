"""ProgrammingClass URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.contrib.auth import views as auth 
import User.views as user_views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("getstudent/", include('GetStudent.urls', namespace='get_student') ),
    path("judger/", include('Judger.urls', namespace='judger') ),
    path("user/", include('User.urls', namespace='user') ),
    path('login/', user_views.login_form, name='login'),
    path('register/', user_views.register, name='register'),
    path('logout/', auth.LogoutView.as_view(template_name ='index.html'), name ='logout'), 
    path('test/', user_views.index, name='index')
    
]