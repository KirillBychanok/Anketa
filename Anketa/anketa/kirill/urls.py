from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('python/', python, name='python'),
    path('django/', django, name='django'),
    path('docker/', docker, name='docker'),
    path('redis/', redis, name='redis'),
    path('soft_and_hard/', soft_and_hard, name='soft_hard'),
    path('experience', experience, name='experience'),
    path('education', education, name='education'),
    path('contacts', contacts, name='contacts'),
]
