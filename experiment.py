from utility.utils import timeit

from src.http.client import make_request_using_http_client



SERVER_IP = "127.0.0.1"  # http://localhost
SERVER_PORT = 8080
# headers = {'Content-type': 'application/octet-stream'}
file_loc_to_write = "/home/aakriti/PycharmProjects/fileTransferProtocols/data/http/client"


@timeit
def file_10kB_10000_times():
    filename = '10kB'
    times=10000
    for i in range(times):
        make_request_using_http_client(SERVER_IP, SERVER_PORT, filename, file_loc_to_write)


@timeit
def file_100kB_1000_times():
    filename = '100kB'
    times=1000
    for i in range(times):
        make_request_using_http_client(SERVER_IP, SERVER_PORT, filename, file_loc_to_write)


@timeit
def file_1MB_100_times():
    filename = '1MB'
    times=100
    for i in range(times):
        make_request_using_http_client(SERVER_IP, SERVER_PORT, filename, file_loc_to_write)


@timeit
def file_10MB_10_times():
    filename = '10MB'
    times=10
    for i in range(times):
        make_request_using_http_client(SERVER_IP, SERVER_PORT, filename, file_loc_to_write)


if __name__ =='__main__':

    file_10kB_10000_times()
    file_100kB_1000_times()
    file_1MB_100_times()
    file_10MB_10_times()