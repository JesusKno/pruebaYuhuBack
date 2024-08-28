from django.urls import path, include
from rest_framework import routers
from taskmanager import views

router = routers.DefaultRouter()

router.register(r'task', views.taskApi)


urlpatterns = [
    path('', include(router.urls))
]