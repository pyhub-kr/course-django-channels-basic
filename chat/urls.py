from django.urls import path
from chat import views

app_name = "chat"

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:room_name>/chat/", views.room_chat, name="room_chat"),
]
