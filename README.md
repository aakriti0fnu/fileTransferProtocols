# fileTransferProtocols

=====
- How to run the project:

  - create & build a virtual environment from `requirement.txt`.

    - **create environment** : `virtualenv --python=3.8 fileTransferProtocols_env38`
    - **source it**          : `source fileTransferProtocols_env38/bin/activate`
    - **load from file**    :  `pip install -r requirements.txt`

  - Install project in editable state `pip install -e .` 
  - Run a server:
     
      `python3 src/<protocol_name>/server.py <file_loc_on_server>`
      
      Example:
        
      ```
      # run ftp server
      python3 src/ftp/server.py data/server

      # run http server
      python3 src/http/server.py data/server
      
      # run smtp server
      python3 src/smtp/server.py data/server
      ```

    Run respective client:

      ```
      python3 src/<protocol_name>/client.py \
                         <filename_to_request> \
              [optional] <drop_loc> \
                         <serverIP>
      ``` 

      Example:

      ```
      # File transfer using FTP protocol.
        python3 src/ftp/client.py 10kB data/client 127.0.0.1
      
      # File transfer using HTTP protocol.
        python3 src/http/client.py 100kB data/client 127.0.0.1
      
      # File transfer using SMTP protocol
        python3 src/smtp/client.py 1MB 0.0.0.0
      ```

  - Run experiments(optional):
    To understand more about the [experiments and implementation details.](./docs/implementation_details.md)

    ```
    bash run.sh
    ```

    - Results:

        - Throughput (in kilo bits per second)

            |           | Throughput  |           |            |           |           |           |           |           |
            |-----------|--------------|-----------|------------|-----------|-----------|-----------|-----------|-----------|
            |           | 10kB file    |           | 100kB file |           | 1MB file  |           | 10MB file |           |
            |           | Average      | Std. Dev. | Average    | Std. Dev. | Average   | Std. Dev. | Average   | Std. Dev. |
            | HTTP      | 279,760.02   | 50,642.04 | 45,837.29  | 22,884.94 | 52,676.63 | 18,629.06 | 65,945.57 | 23,118.25 |
            | FTP       | 4,333.99     | 882.093   | 18,315.71  | 4,185.18  | 50,902.27 | 7,330.37  | 81,034.39 | 4,942.01  |
            | SMTP      | 1,385.86     | 394.568   | 3,070.23   | 533.651   | 3,453.45  | 322.877   | 3,524.77  | 228.911   |
        
        - Total application layer data transferred from sender to receiver (including header content) per file divided by the file size (for Bittorent, further multiply with 3)

            |           | Total application layer data  |            |          |           |
            |-----------|--------------------------------|------------|----------|-----------|
            |           | 10kB file                      | 100kB file | 1MB file | 10MB file |
            |           | Average                        | Average    | Average  | Average   |
            | HTTP      | 1                              | 1          | 1        | 1         |
            | FTP       | 1                              | 1          | 1        | 1         |
            | SMTP      | 1.273                          | 1.372      | 1.368    | 1.369     |


Notes:

  - Transferred files filesize in bytes(per file)
    ```
    10kB = 10240
    100kB = 102400
    1MB = 1048576
    10MB = 10485760
    ```
Future work:

  - implement bit-torrent