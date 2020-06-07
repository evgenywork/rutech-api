"""rutech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/base-auth/', include('rest_framework.urls')),
    path('api/v1/account/', include('account.urls')),
    path('api/v1/conversations/', include('conversation.urls')),
    path('api/v1/rooms/', include('room.urls')),
    path('api/v1/messages/', include('message.urls')),
    path('api/v1/backgrounds/', include('background.urls')),
    path('api/v1/events/', include('event.urls')),
    path('api/v1/tags/', include('tag.urls')),
    path('api/v1/networkings/', include('networking.urls')),

]
