from django.urls import path
from aichiworks import views

app_name = 'aichiworks'

urlpatterns = [
    path('', views.index, name='index'),
    path('aichiworks', views.index, name='index'),
    path('aichiworks/<str:orderNum>', views.detail, name='index'),
    path('<str:orderNum>', views.detail, name='index')
]
