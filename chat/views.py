from django.shortcuts import render, redirect

from chat.forms import RoomForm


def index(request):
    return render(request, "chat/index.html")


def room_new(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            created_room = form.save()
            return redirect("chat:room_chat", created_room.pk)
    else:
        form = RoomForm()

    return render(request, "chat/room_form.html", {
        "form": form,
    })


def room_chat(request, room_name):
    return render(request, "chat/room_chat.html", {
        "room_name": room_name,
    })
