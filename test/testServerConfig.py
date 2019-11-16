from src.serverConfig import ServerConfig


class TestServerConfig:

    def test_serverPort_is_localhost(self):
        server = ServerConfig()
        serverPort = server.startServer()
        assert serverPort == 8080

