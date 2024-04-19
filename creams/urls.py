from django.urls import path
from . import views

app_name = 'creams'
urlpatterns = [
    path('',views.index, name= 'index')
]
