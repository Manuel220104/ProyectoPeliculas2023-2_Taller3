from django.urls import path
from . import views

urlpatterns = [
    path('recommendations/', views.recommendation_view, name='recommendations'),  
]
