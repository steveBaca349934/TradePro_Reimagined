from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
    path('RAT', index),
    path('About', index),
    path('News', index),
    path('MeetTheTeam', index)


]