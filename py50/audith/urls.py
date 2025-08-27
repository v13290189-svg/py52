from django.urls import path
from . import views # Импотртиреум из ЭТОЙ ЖЕ ПАПКИ ПРИЛОЖЕНИЯ файл views

# В файле urls.py КОНКРЕТНОГО приложения, маршрутизации считается, начиная с адреса
# ПРИЛОЖЕНИЯ. Например, этот файл находить в папке audith, и подключен в
# глобальный urls.py всего проекта -> все адреса, описанные в этом файле, УЖЕ ПО УМОЛЧАНИЮ
# начинаются с адреса 127.0.0.1:8000/audith

urlpatterns = [
    path('', views.index, name="audith"),
    path('about/', views.about, name="about"),
]