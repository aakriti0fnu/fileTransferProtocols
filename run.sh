#!/bin/bash
# echo Experiment:FTP
# for i in {1..100}
# do
#    python3 src/ftp/client.py 10kB data/client 127.0.0.1
# done

# echo 

# echo Experiment:HTTP
# for i in {1..100}
# do
#    python3 src/http/client.py 100kB data/client 127.0.0.1
# done

echo 

echo Experiment:SMTP

for i in {1..100}
do
   python3 src/smtp/client.py 1MB data/client 127.0.0.1
done
