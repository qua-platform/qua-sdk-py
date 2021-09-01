import pytest


def pytest_addoption(parser):
    parser.addoption("--server_host", action="store", default="127.0.0.1")
    parser.addoption("--server_port", action="store", default=9510)


def pytest_generate_tests(metafunc):
    # This is called for every test. Only get/set command line arguments
    # if the argument is specified in the list of test "fixturenames".
    for param in ["server_host", "server_port"]:
        value = getattr(metafunc.config.option, param)
        if param in metafunc.fixturenames and value is not None:
            metafunc.parametrize(param, [value])


@pytest.fixture(scope="function")
def qua_client(server_host, server_port):
    from qua import QuaClient
    return QuaClient(host=server_host, port=server_port)
