from .views import index_view, contacts_view, catalog_view
from django.urls import path




urlpatterns = [path('', index_view, name='index'),
               path('contacts/', contacts_view, name='contacts'),
               path('collection/<str:slug>/', catalog_view, name='collection'),
               ]
