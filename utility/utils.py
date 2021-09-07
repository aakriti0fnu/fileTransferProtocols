import time
from typing import Protocol

import csv

import datetime


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        time_took=te - ts
        print(f">>> {method.__name__} took {time_took}.")

        protocol=''
        if method.__name__.startswith( 'ftp' ):
            protocol= 'ftp'
        if method.__name__.startswith( 'http' ):
            protocol= 'http'
        if method.__name__.startswith( 'smtp' ):
            protocol= 'smtp'

        with open(f'logs/{protocol}_logtime.csv', 'a') as f:
            writer = csv.writer(f)
            now = datetime.datetime.now()
            # "%H:%M:%S.%f"
            writer.writerow([f"{now.strftime('%Y-%m-%d %H:%M:%S.%f')} || {str(time_took)} "])

        return result
    return timed





def logtime(method):
    def timed(*args, **kw):

        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        
        print(f">>> {method.__name__} took {te - ts}.")
        return result
    return timed
