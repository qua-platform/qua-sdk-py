from grpclib.client import Channel
from qua.grpc.io.qualang.api.v1 import InfoServiceStub
from qua.info import QuaMachineInfo, ImplementationInfo


class QuaClient:
    def __init__(self, *, host: str = "127.0.0.1", port: int = 80, **kwargs) -> None:
        self._host = host
        self._port = port
        self._channel_factory = kwargs.get("grpc_channel_factory", None)
        super().__init__()

    def _create_channel(self):
        if self._channel_factory is not None:
            return self._channel_factory()
        else:
            return Channel(host=self._host, port=self._port)

    async def get_server_info(self):
        async with self._create_channel() as channel:
            service = InfoServiceStub(channel)
            response = await service.get_info()
            return QuaMachineInfo(
                capabilities=response.capabilities,
                implementation=ImplementationInfo(
                    name=response.implementation.name,
                    version=response.implementation.version,
                    url=response.implementation.url,
                ),
            )
