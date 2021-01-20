from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("map", views.map, name="map"),
    path("mypage", views.mypage, name="mypage"),
    path("register", views.register, name="register"),
    path("register_cat", views.register_cat, name="register_cat"),
    path("chatting", views.chatting, name="chatting"),
    path("image_test", views.image_test, name="image_test"),
    path("info_cat", views.info_cat, name="info_cat"),
    path("info_kitchen", views.info_kitchen, name="info_kitchen"),
]
