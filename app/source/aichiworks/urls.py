from django.urls import path
from aichiworks import views

app_name = 'aichiprworks'

urlpatterns = [
    path('', views.index, name='index'),
    path('process', views.show_process, name='process'),
    path('process/message', views.show_message, name='message_ajax'),
    path('<str:orderNum>', views.detail, name='detail'),
    path('util/showDatabase', views.show_database, name='util'),
    path('util/addProcess', views.add_process_render, name='util'),
    path('util/deleteProcess', views.delete_process_render, name='util'),
    path('util/sendMessage', views.send_message_render, name='util'),
    path('util/deleteMessage', views.delete_message_render, name='util'),
    path('util/editProcess/<str:processID>', views.edit_process_render, name='editProcess'),
]
