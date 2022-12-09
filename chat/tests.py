import pytest
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.security.websocket import OriginValidator
from channels.testing import WebsocketCommunicator


@pytest.mark.it("OriginValidator 설정값 테스트")
@pytest.mark.parametrize(
    ("allowed_origins", "origin_header", "expect_connected"),
    [
        (["http://localhost:8000"], "http://localhost:9000", False),
        (["localhost:9000"], "http://localhost:9000", False),
        (["localhost"], "http://localhost:9000", True),
    ]
)
@pytest.mark.asyncio
async def test_origin_validator_settings(allowed_origins, origin_header, expect_connected):
    application = OriginValidator(AsyncWebsocketConsumer(), allowed_origins)

    if origin_header is None:
        headers = []
    else:
        if isinstance(origin_header, str):
            origin_header = origin_header.encode("latin-1")
        headers = [
            (b"origin", origin_header),
        ]

    communicator = WebsocketCommunicator(application, "/", headers=headers)
    connected, __ = await communicator.connect()
    assert connected == expect_connected
    await communicator.disconnect()
