from django.urls import path
from .views import home
from .views import home, submit_form, user_list

urlpatterns = [
    path('', home, name='home'),
    path('submit/', submit_form, name='submit_form'),
    path('users/', user_list, name='user_list'),
]
