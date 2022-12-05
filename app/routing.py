from django.urls import path
from app.consumers import EchoConsumer, LiveblogConsumer

websocket_urlpatterns = [
    path("ws/liveblog/", LiveblogConsumer.as_asgi()),
    path("ws/echo/", EchoConsumer.as_asgi()),
]
