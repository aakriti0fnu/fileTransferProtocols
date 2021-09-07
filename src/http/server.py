import os
import sys
from http.server import BaseHTTPRequestHandler,HTTPServer

server_data_loc= sys.argv[1]

class myServer(BaseHTTPRequestHandler):

    def read_file(self, file_to_read):
        for dir_name, sub_dirs, filenames in os.walk(server_data_loc):
            if not sub_dirs:
                if file_to_read in filenames:
                    print(f"{file_to_read} exist on server")
                    file_loc = os.path.join(dir_name, file_to_read)
                    # read file in to a fileobject
                    read_file_obj = open(file_loc, 'rb')
                    return read_file_obj
                else:
                    print(f"{file_to_read} not exist on server")

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

        read_file_obj= self.read_file(file_from_client)
        # read content of the file in bytes!(default whole file!)
        bytes_to_send = read_file_obj.read()
        # write content on io.buffered
        self.wfile.write(bytes_to_send)
        pass

    def do_POST(self):
        self.rfile.read()
        pass


if __name__=='__main__':

    SERVER_IP = "127.0.0.1" #http://localhost
    SERVER_PORT = 8080
    ADDR =(SERVER_IP, SERVER_PORT)
    my_server = HTTPServer(server_address=ADDR, RequestHandlerClass=myServer)
    print("Starting http Server")
    my_server.serve_forever()

# import os
# import time
# import csv

# from http.server import BaseHTTPRequestHandler,HTTPServer,ThreadingHTTPServer,SimpleHTTPRequestHandler
# server_data_loc= os.getcwd()


# class myServer(BaseHTTPRequestHandler):
#     def do_GET(self):
#         self.send_response(200)
#         self.send_header('Content-Type',
#                          'application/octet-stream')
#         self.end_headers()
#         #print('*'*5)
#         #print(self.command)
#         #print(self.path)
#         #print(self.request_version)
#         #print(self.headers)
#         #print('*' * 5)

#         file_from_client= self.path.split('/')[1]
#         #print("File needed from client",file_from_client)

#         file_loc = os.path.join(server_data_loc, file_from_client)
#         #print(str(file_loc))

#         # Append execution time to csv & print to console
#         with open(file_loc, 'rb') as file:
#             tic = time.perf_counter()
#             self.wfile.write(file.read()) # Read the file and send the contents
#             toc = time.perf_counter()
#             tm = toc-tic
#             print(f"Elapsed time: {toc - tic:0.8f} seconds")
#             with open('HTTPdata.csv', 'a') as f:
#                 writer = csv.writer(f)
#                 writer.writerow([str(tm)])

#     def do_POST(self):
#         pass

if __name__=='__main__':
    SERVER_IP = "0.0.0.0"
    SERVER_PORT = 8080
    ADDR =(SERVER_IP, SERVER_PORT)
    my_server = HTTPServer(server_address=ADDR, RequestHandlerClass=myServer)
    print("Starting HTTP Server")
    print("Server running...")
    my_server.serve_forever()