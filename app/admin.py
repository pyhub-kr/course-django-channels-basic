from django.contrib import admin
from app.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
