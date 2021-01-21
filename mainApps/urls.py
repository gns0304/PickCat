from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views, mentions

urlpatterns = [
    path("main", views.main, name="main"),
    path("map", views.map, name="map"),
    path("mypage", views.mypage, name="mypage"),
    path("register", views.register, name="register"),
    path("register_cat", views.register_cat, name="register_cat"),
    path("register_kitchen/<int:kitchen_id>",
         views.register_kitchen, name="register_kitchen"),
    path("chatting", views.chatting, name="chatting"),
    path("image_test", views.image_test, name="image_test"),
    path("", views.intro, name="intro"),
    path("info_cat/<int:cat_id>", views.info_cat, name="info_cat"),
    path("info_kitchen/<int:kitchen_id>",
         views.info_kitchen, name="info_kitchen"),
    path("login", views.login, name="login"),
    path("sign_up", views.sign_up, name="sign_up"),
    path("sign_out", views.sign_out, name="sign_out"),
    path("emergency", mentions.newEmergencyMention, name="emergency"),
    path("getCatMentions", mentions.getCatMentions, name="getCatMentions"),
    path("getKitchenMentions", mentions.getCatMentions, name="getKitchenMentions"),
    path("addfavoritecat/<int:thisCat_id>",
         views.addFavoriteCat, name="addFavoriteCat"),
    path("removefavoritecat/<int:thisCat_id>",
         views.removeFavoriteCat, name="removeFavoriteCat"),
    path("addfavorietkitchen/<int:thisKitchen_id>",
         views.addFavoriteKitchen, name="addFavoriteKitchen"),
    path("removefavoritekitchen/<int:thisKitchen_id>",
         views.removeFavoriteKitchen, name="removeFavoriteKitchen"),
    path("mention_kitchen/<int:thisKitchen_id>",
         views.mention_kitchen, name="mention_kitchen"),
    path("join1", views.join1, name="join1"),
    path("join2", views.join2, name="join2"),
    path("join3", views.join3, name="join3"),
    path("join4", views.join4, name="join4"),

    path("sign_up", views.sign_up, name="sign_up"),
    path("sign_out", views.sign_out, name="sign_out"),
    path("emergency", mentions.newEmergencyMention, name="emergency"),
    path("getCatMentions", mentions.getCatMentions, name="getCatMentions"),
    path("getKitchenMentions", mentions.getCatMentions, name="getKitchenMentions"),
    path("newCatMentions", mentions.getCatMentions, name="newCatMentions"),
    path("newKitchenMentions", mentions.getCatMentions, name="newKitchenMentions"),
    path(
        "addfavoritecat/<int:thisCat_id>", views.addFavoriteCat, name="addFavoriteCat"
    ),
    path(
        "removefavoritecat/<int:thisCat_id>",
        views.removeFavoriteCat,
        name="removeFavoriteCat",
    ),
    path("addfavoritecat/<int:thisCat_id>",
         views.addFavoriteCat, name="addFavoriteCat"),
    path("removefavoritecat/<int:thisCat_id>",
         views.removeFavoriteCat, name="removeFavoriteCat"),
    path("mention_kitchen", views.mention_kitchen, name="mention_kitchen"),
    path("read_qr", views.read_qr, name="read_qr"),
    path("newChat", mentions.newChat, name="newChat"),
    path("getChat", mentions.getChat, name="getChat"),
    path("newchat", views.newchat, name="newchat")

]
