import os
import io
from http.server import BaseHTTPRequestHandler,HTTPServer,ThreadingHTTPServer,SimpleHTTPRequestHandler

server_data_loc= "/home/aakriti/PycharmProjects/fileTransferProtocols/data/http/server"

class myServer(BaseHTTPRequestHandler):

    def do_GET(self):

        self.send_response(200)
        self.send_header('Content-Type',
                         'application/octet-stream')
        self.end_headers()
        # print('*'*5)
        # print(self.command)
        # print(self.path)
        # print(self.request_version)
        # print(self.headers)
        # print('*' * 5)

        file_from_client= self.path.split('/')[1]
        print("File needed from client",file_from_client)

        for dir_name, sub_dirs, filenames in os.walk(server_data_loc):
            if not sub_dirs:
                if file_from_client in filenames:
                    print(f"{file_from_client} exist on server")
                    file_loc = os.path.join(dir_name, file_from_client)
                    # read file in to a fileobject
                    read_file_obj = open(file_loc, 'rb')
                    # read content of the file in bytes!(default whole file!)
                    bytes_to_send = read_file_obj.read()
                    # write content on io.buffered
                    # https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.wfile
                    self.wfile.write(bytes_to_send)
                else:
                    print(f"{file_from_client} not exist on server")


        pass

    def do_POST(self):
        self.rfile.read()
        pass


if __name__=='__main__':

    SERVER_IP = "127.0.0.1"#http://localhost
    SERVER_PORT = 8080
    ADDR =(SERVER_IP, SERVER_PORT)

    my_server = HTTPServer(server_address=ADDR, RequestHandlerClass=myServer)
    # SimpleHTTPRequestHandler(directory=server_data_loc)
    print("Starting http Server")
    my_server.serve_forever()