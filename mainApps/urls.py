from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path("main", views.main, name="main"),
    path("map", views.map, name="map"),
    path("mypage", views.mypage, name="mypage"),
    path("register", views.register, name="register"),
    path("register_cat", views.register_cat, name="register_cat"),
    path("register_kitchen", views.register_kitchen, name="register_kitchen"),
    path("chatting", views.chatting, name="chatting"),
    path("image_test", views.image_test, name="image_test"),
    path("", views.intro, name="intro"),
    path("info_cat", views.info_cat, name="info_cat"),
    path("info_kitchen", views.info_kitchen, name="info_kitchen"),
    path("login", views.login, name="login"),
    path("join1", views.join.join1, name="join1"),
    path("join2", views.join.join2, name="join2"),
    path("join3", views.join.join3, name="join3"),
    path("join4", views.join.join4, name="join4"),

]
