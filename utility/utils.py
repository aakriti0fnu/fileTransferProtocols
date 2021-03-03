import time

def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print("{} took {}.".format(method.__name__,time.strftime("%H:%M:%S" , time.gmtime((te - ts))) ))
        # logging.info(msg= "{} took {}.".format(method.__name__,time.strftime("%H:%M:%S" , time.gmtime((te - ts))) ) )
        return result
    return timed