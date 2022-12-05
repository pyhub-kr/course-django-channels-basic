import json

from channels.generic.websocket import WebsocketConsumer


class LiveblogConsumer(WebsocketConsumer):
    groups = ["liveblog"]

    def liveblog_post_created(self, event_dict):
        self.send(json.dumps(event_dict))

    def liveblog_post_updated(self, event_dict):
        self.send(json.dumps(event_dict))

    def liveblog_post_deleted(self, event_dict):
        self.send(json.dumps(event_dict))


class EchoConsumer(WebsocketConsumer):

    def receive(self, text_data=None, bytes_data=None):
        obj = json.loads(text_data)
        print("수신 :", obj)

        json_string = json.dumps({
            "content": obj["content"],
            "user": obj["user"],
        })
        self.send(json_string)
