import os
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from exception import ftp_exit


def start_ftp_server(ftp_tuple):
    host, port, user, password, path = ftp_tuple

    port = int(port)
    if user == "":
        ftp_exit(1, "User is empty")
        pass
    if not (1 <= port <= 65535):
        ftp_exit(1, "Port is invalid")
        pass

    if path == '':
        path = "./"
        pass

    authorizer = DummyAuthorizer()
    authorizer.add_user(user, password, path, perm='elradfmw')

    handler = FTPHandler
    handler.authorizer = authorizer

    if host != '':
        handler.masquerade_address = host
        
    handler.passive_ports = range(50000,51000)

    server = FTPServer(('0.0.0.0', port), handler)
    print("FTP Server Start")
    server.serve_forever()
    ftp_exit(0, "FTP Server Exit")
