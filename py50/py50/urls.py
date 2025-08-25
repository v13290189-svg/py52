"""
URL configuration for py50 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,include

# Хост проекта по умолчанию - 127.0.0.1:8000

urlpatterns = [
    path('admin/', admin.site.urls),
    # path() - встроеный метод в Django, для преобразования и получения пути из тела запроса
    # path() имеет два обязательных аргумента: путь относительно хоста проекта и файл маршрутизации
    # include() - встроенный метод в Django, для подключения файла маршрутизации (urls.py)
    # include() - имеет один обязательный аргумент: путь до файла urls приложения в формате 'app_name.urls'
    path('audith/', include('audith.urls')),
]
