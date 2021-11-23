from django.urls import path

from . import views

"""
URL Patterns include 
'/fizzbuzz' - loads FizzBuzzView
'/fizzbuzz/<int>' - loads FizzBuzzDetail where <int> is the id of a stored entry
'' - another location for FizzBuzzView 
"""
urlpatterns = [
    path('fizzbuzz', views.FizzBuzzView.as_view(),
        name='fizzbuzz'),
    path('fizzbuzz/<int:pk>', views.FizzBuzzDetail.as_view(),
        name='fizzdetail'),
    path('', views.FizzBuzzView.as_view(),
        name='fizzhome'),
]
