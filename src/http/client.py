import http.client as client
import os
import traceback

def make_request_using_http_client(ip, port, filename, file_loc_to_write):
    try:
        conn = client.HTTPConnection(ip, port)
        # make a request for a file!
        conn.request('GET', f'/{filename}')
        # parse the response from server!
        try:
            response= conn.getresponse()
            # print(response.status, response.reason)
            file_to_write = os.path.join(file_loc_to_write,filename)
            file_data = response.read()
            # print(f"filecontent type{type(file_data)}, and size in bytes {len(file_data)}" )
            # create new file, to receive
            FSTREAM = open(file_to_write, "wb")
            FSTREAM.write(file_data)
            FSTREAM.close()
            # print('file retrieved')
        except Exception:
            print(traceback.format_exc())
    except:
        raise

    pass

def make_request_using_urllib3():
    '''
    request is http client for python
    :return:
    '''

    pass

if __name__=='__main__':

    SERVER_IP = "127.0.0.1"  # http://localhost
    SERVER_PORT = 8080
    # headers = {'Content-type': 'application/octet-stream'}

    # make_request_using_urllib3()
    filename = '100kB'
    file_loc_to_write = "/home/aakriti/PycharmProjects/fileTransferProtocols/data/http/client"
    make_request_using_http_client(SERVER_IP,SERVER_PORT ,filename, file_loc_to_write)



