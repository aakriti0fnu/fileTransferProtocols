import sys

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

server_data_loc= sys.argv[1]

def ftp_server(address):
    '''
    :param address: (SERVER_IP, SERVER_PORT)
    :return:
    '''

    authorizer = DummyAuthorizer()
    try:
        # add user to the virtual users table
        # authorizing a user with file access to a directory on server.
        # Read permissions:
        #       "l" = list files (LIST, NLST, STAT, MLSD, MLST, SIZE commands)
        #       "r" = retrieve file from the server (RETR command)
        authorizer.add_user(username="dummy_user", password="12345", homedir= server_data_loc, perm="lr", msg_login="Logged IN", msg_quit="Logged OUT")
    except Exception:
        print("insufficient permissions or duplicate usernames")
        raise Exception

    # Handling Client's request!
    handler = FTPHandler
        # verify user’s password,
        # gets users home directory,
        # checking user permissions when a filesystem read event occurs and
        # changing user before accessing the filesystem.
    handler.authorizer = authorizer
    handler.banner= f"FTP_server is ready to listen"
    server = FTPServer(address, handler) # can't suppress this message- default msg displays!
    # Starting FTP server
    server.serve_forever()


if __name__=='__main__':
    SERVER_IP = "127.0.0.1" # http://localhost
    SERVER_PORT = 2121 # must be > 1023
    ftp_server( (SERVER_IP, SERVER_PORT))