import time

def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print("{} took {}.".format(method.__name__,te - ts))
        return result
    return timed