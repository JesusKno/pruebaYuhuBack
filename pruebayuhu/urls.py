"""
URL configuration for pruebayuhu project.

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
from django.urls import path, include
from taskmanager import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signUp/', views.signUp, name='signup'),
    path('home/', views.home, name='home'),
    path('logout/', views.singOut, name='logout'),
    path('signIn/', views.signIn, name='signin'),
    path('task/create/', views.newtask, name='newtask'),
    path('task/<int:task_id>/update', views.updatetask, name='updatetask'),
    path('task/<int:task_id>/delete', views.deletetask, name='deletetask'),
    path('api/', include('taskmanager.urlapi'))
]
