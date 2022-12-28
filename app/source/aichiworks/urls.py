from django.urls import path
from aichiworks import views

app_name = 'aichiprworks'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:orderNum>', views.detail, name='index'),
    path('util/showDatabase', views.show_database, name='index'),
    path('util/addProcess', views.add_process_render, name='index'),
    path('util/deleteProcess', views.delete_process_render, name='index'),
    path('util/sendMessage', views.send_message_render, name='index'),
    path('util/deleteMessage', views.delete_message_render, name='index'),
    path('util/editProcess/<str:processID>', views.edit_process_render, name='editProcess'),
]
