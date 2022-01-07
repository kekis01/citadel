from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='Citadel'),
    path('news/', news, name='news'),
    path('media/', video, name='media'),
    path('photos/', photos, name='photos'),
    path('player/', player, name='player'),
    path('streams/', streams, name='streams'),
    path('video/', video, name='video'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('registration/', RegisterUser.as_view(), name='registration'),
    path('tournaments/', tournaments, name='tournaments'),
    path('info/', info, name='info'),
    path('shop/', shop, name='shop'),
    path('article/<int:artid>/', article, name='article'),
]
