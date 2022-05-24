from django.urls import path
from . import views

urlpatterns = [
    path('', views.find_most_similar, name='most_similar_words'),
]
