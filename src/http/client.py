import http.client as client
import os
import sys
import traceback

from utility.utils import timeit

@timeit
def http_server_request(conn):
    
    conn.request('GET', f'/{filename}')
    # parse the response from server!
    try:
        response= conn.getresponse()
    except Exception:
        print(traceback.format_exc())
    return response

def make_request_using_http_client(ip, port, filename, file_loc_to_write):
    try:
        conn = client.HTTPConnection(ip, port)
        # make a request for a file!
        response= http_server_request(conn)

        # print(response.status, response.reason)
        file_to_write = os.path.join(file_loc_to_write, f"retrieved_{filename}")
        file_data = response.read()
        print(f"filecontent type{type(file_data)}, and size in bytes {len(file_data)}" )
        # create new file, to receive
        FSTREAM = open(file_to_write, "wb")
        FSTREAM.write(file_data)
        FSTREAM.close()
        # print('file retrieved')
    except:
        raise
    pass

def make_request_using_urllib3():
    '''
    Could use `requests `
    https://www.datacamp.com/community/tutorials/making-http-requests-in-python
    request is http client for python
    
    :return:
    '''
    pass

if __name__=='__main__':

    SERVER_PORT = 8080
    # headers = {'Content-type': 'application/octet-stream'}
    # make_request_using_urllib3()

    filename = sys.argv[1]
    file_loc_to_write = sys.argv[2]
    SERVER_IP = sys.argv[3] # "127.0.0.1" #http://localhost

    make_request_using_http_client(SERVER_IP,SERVER_PORT ,filename, file_loc_to_write)