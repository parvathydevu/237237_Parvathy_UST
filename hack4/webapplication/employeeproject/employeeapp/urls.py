
from django.urls import path
from . import views

urlpatterns = [
    path('salary_form/', views.input, name='salary_form'),
    path('result/', views.result, name='result'),
    path('jumble_words/', views.jumble_words, name='jumble_words'),
]

