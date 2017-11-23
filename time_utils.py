import time

def ti(function):
    def _ti(*args, **kargs):
        start = time.time()
        function(*args, **kargs)
        print "function %s use: %f" % (function.__name__, time.time() - start)

    return _ti
    

