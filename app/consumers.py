import json

from channels.generic.websocket import JsonWebsocketConsumer


class LiveblogConsumer(JsonWebsocketConsumer):
    groups = ["liveblog"]

    def liveblog_post_created(self, event_dict):
        self.send_json(event_dict)

    def liveblog_post_updated(self, event_dict):
        self.send_json(event_dict)

    def liveblog_post_deleted(self, event_dict):
        self.send_json(event_dict)


class EchoConsumer(JsonWebsocketConsumer):

    def receive_json(self, content, **kwargs):
        print("수신 :", content)

        self.send_json({
            "content": content["content"],
            "user": content["user"],
        })
