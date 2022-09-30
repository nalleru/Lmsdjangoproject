from django.urls import path

from users.views import Profile, requests

app_name = 'users'

urlpatterns = [
    path('profile/', Profile, name='profile'),
    path('requests/', requests, name='requests'),

]