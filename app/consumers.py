from channels.generic.websocket import WebsocketConsumer


class EchoConsumer(WebsocketConsumer):

    def receive(self, text_data=None, bytes_data=None):
        self.send(f"You said : {text_data}")
