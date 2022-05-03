import socket

class Server:
    """
    Get the public/LAN IP of the serving device.
    """
    def __init__(self):
        self.ip = "127.0.0.1" # deafualt to localhost
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # attemp a connection so we can read our IP from the socket.
            self._socket.connect(("1.1.1.1", 1)) # does not have to be reachable (e.g. on a LAN)
            self.ip = self._socket.getsockname()[0] # set the IP
        finally:
            # whatever happens, close the socket.
            self._socket.close()
