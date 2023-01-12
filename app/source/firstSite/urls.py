"""firstSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aichiprworks/', include('aichiworks.urls')),
    path('aichiprworks/<str:orderNum>', include('aichiworks.urls')),
    path('aichiprworks/process', include('aichiworks.urls')),
    path('aichiprworks/process/message/', include('aichiworks.urls')),
    path('aichiprworks/process/delete_process/', include('aichiworks.urls')),
    path('aichiprworks/process/changeStatus/', include('aichiworks.urls')),
    path('aichiprworks/util/showDatabase', include('aichiworks.urls')),
    path('aichiprworks/util/addProcess', include('aichiworks.urls')),
    path('aichiprworks/util/deleteProcess', include('aichiworks.urls')),
    path('aichiprworks/util/sendMessage', include('aichiworks.urls')),
    path('aichiprworks/util/deleteMessage', include('aichiworks.urls')),
    path('aichiprworks/util/editProcess/<str:processID>', include('aichiworks.urls')),
    path('rbworks/', include('rbworks.urls')),
]
