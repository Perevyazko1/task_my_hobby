from django.urls import path

from .views import about_me, contacts, home

urlpatterns = [
    path('', home, name='home'),
    path('about_me/', about_me, name='about_me'),
    path('contacts/', contacts, name='contacts'),

]