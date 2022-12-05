from django.shortcuts import render


def index(request):
    return render(request, "chat/index.html")


def room_chat(request, room_name):
    return render(request, "chat/room_chat.html", {
        "room_name": room_name,
    })
