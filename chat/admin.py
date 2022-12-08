from django.contrib import admin
from chat.models import Room


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass
