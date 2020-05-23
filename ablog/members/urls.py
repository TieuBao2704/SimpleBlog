from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'members'

urlpatterns = [
    path('register/', views.UserRegister.as_view(), name = 'register'),
    # path('login'),

]
