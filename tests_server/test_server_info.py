import pytest


@pytest.mark.asyncio
async def test_info_received(qua_client):
    await qua_client.get_server_info()
