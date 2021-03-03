import hashlib


# Code to verify file transfer using checksum!

server_file = "/data/http/server/10kB"
client_file= "/data/http/client/10kB"
new =  hashlib.md5( open(client_file,'rb').read() ).hexdigest()
orig=  hashlib.md5( open(server_file,'rb').read() ).hexdigest()

if orig == new:
    print("matched")
    print(new+'\n'+orig)
else:
    print("not matched")
    print(new+'\n'+orig)