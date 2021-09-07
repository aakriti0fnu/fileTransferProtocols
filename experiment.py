from utility.utils import timeit

from src.http.client import make_request_using_http_client
from src.ftp.client import make_request_ftp_client


# For Http:
SERVER_IP = "127.0.0.1"  # http://localhost
HTTP_SERVER_PORT = 8080
# headers = {'Content-type': 'application/octet-stream'}
http_loc_to_write = "data/http/client"


# For FTP
SERVER_IP = "127.0.0.1"  # http://localhost
FTP_SERVER_PORT = 2121
ftp_loc_to_write = "data/ftp/client"


# file transfer takes, divide the file size by this time, and record the result
@timeit
def file_10kB_10000_times():
    filename = '10kB'
    times=10000
    for i in range(times):
        make_request_using_http_client(SERVER_IP, HTTP_SERVER_PORT, filename, http_loc_to_write)
        # make_request_ftp_client(SERVER_IP, FTP_SERVER_PORT, filename, ftp_loc_to_write)


@timeit
def file_100kB_1000_times():
    filename = '100kB'
    times=1000
    for i in range(times):
        make_request_using_http_client(SERVER_IP, HTTP_SERVER_PORT, filename, http_loc_to_write)
        # make_request_ftp_client(SERVER_IP, FTP_SERVER_PORT, filename, ftp_loc_to_write)


@timeit
def file_1MB_100_times():
    filename = '1MB'
    times=100
    for i in range(times):
        make_request_using_http_client(SERVER_IP, HTTP_SERVER_PORT, filename, http_loc_to_write)
        # make_request_ftp_client(SERVER_IP, FTP_SERVER_PORT, filename, ftp_loc_to_write)


@timeit
def file_10MB_10_times():
    filename = '10MB'
    times=10
    for i in range(times):
        make_request_using_http_client(SERVER_IP, HTTP_SERVER_PORT, filename, http_loc_to_write)
        # make_request_ftp_client(SERVER_IP, FTP_SERVER_PORT, filename, ftp_loc_to_write)


if __name__ =='__main__':

    file_10kB_10000_times()
    file_100kB_1000_times()
    file_1MB_100_times()
    file_10MB_10_times()