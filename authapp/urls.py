from .views import login, logout, edit, register
from django.urls import path
from mainapp.views import index_view

app_name = 'authapp'
urlpatterns = [path('', index_view, name='index'),
               path('login/', login, name='login'),
               path('logout/', logout, name='logout'),
               path('register/', register, name='register'),
               path('edit/', edit, name='edit'),
               ]
