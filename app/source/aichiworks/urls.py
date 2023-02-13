from django.urls import path
from aichiworks import views

app_name = 'aichiprworks'

urlpatterns = [
    path('', views.index, name='index'),
    #path('process', views.show_process, name='process'),
    path('message', views.show_message, name='message_ajax'),
    path('message/send', views.send_message_ajax ,name='message_send_ajax'),
    #path('process/deleteProcess', views.delete_process_ajax, name='delete_process_ajax'),
    #path('process/changeStatus', views.change_status_ajax, name='change_status_ajax'),
    path('detail/<str:orderNum>', views.detail, name='detail'),
    path('util/showDatabase', views.show_database, name='util'),
    #path('util/addProcess', views.add_process_render, name='util'),
    path('util/deleteProcess', views.delete_process_render, name='util'),
    path('util/sendMessage', views.send_message_render, name='util'),
    path('util/deleteMessage', views.delete_message_render, name='util'),
    #path('util/editProcess/<str:processID>', views.edit_process_render, name='editProcess'),
]
