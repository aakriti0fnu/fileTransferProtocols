from ftplib import FTP
import os

def make_request_ftp_client(IP, port, filename, file_loc_to_write):
    '''
    Using ftplib — FTP protocol client.
    :param address:
    :param filename:
    :param file_loc_to_write:
    :return:
    '''
    # Connect to server
    try:
        ftp = FTP()
        ftp.connect(host=IP, port=port)
        ftp.login(user="aaakrit", passwd="12345")
        # catch welcome message from server.
        print(ftp.getwelcome())

    except Exception:
        raise Exception

    file_to_write = os.path.join(file_loc_to_write, filename)
    client_file = open(file_to_write, 'wb')

    # requesting sever for a file and parsing it's response!
    command = f'RETR {filename}'
    response= ftp.retrbinary(command, client_file.write )

    if response.startswith('226'):
        print('File Transfered!')
    else:
        print("Transfer didn't happen")

    client_file.close()
    ftp.close()


if __name__=='__main__':

    SERVER_IP = "127.0.0.1" #http://localhost
    SERVER_PORT = 2121
    filename = '10MB'
    file_loc_to_write = "/home/aakriti/PycharmProjects/fileTransferProtocols/data/ftp/client"
    make_request_ftp_client( SERVER_IP,SERVER_PORT, filename, file_loc_to_write)