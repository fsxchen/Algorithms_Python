'''
@Author: yangxingchen
@Date: 2017-08-19 16:23:20
@LastEditors: yangxingchen
@LastEditTime: 2020-03-20 19:02:06
@Description: 
'''
import time

def ti(function):
    def _ti(*args, **kargs):
        start = time.time()
        function(*args, **kargs)
        print("function %s use: %f" % (function.__name__, time.time() - start))
    return _ti
    

