from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name = 'about'),
    path('login', views.login, name = 'login'),
    path('create', views.create, name = 'create')

]
