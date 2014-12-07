#!-*- coding:utf-8 -*-

import time
import functools

def elapsed(logger=None,verbose="elapsed time: %f ms"):
    """
    Tell us a function performed how many milliseconds.
    if logger is given,it will write in the logger,otherwith 
    it will use print method.
    the verbose is logger format,must have a %f falg.
    """
    def _elapsed(func):
        @functools.wraps(func)
        def _elapsed(*args,**kw):
            start = time.time()
            func(*args,**kw)
            end = time.time()
            secs = end - start
            msecs = secs * 1000
            if logger:
                logger.debug(verbose % msecs)
            else:
                print verbose % msecs
        return _elapsed
    return _elapsed


if __name__ == "__main__":
    @elapsed()
    def add(a,b):
        print a+b
    @elapsed(verbose="the bad function %f:")
    def min(a,b):
        print a-b
    add(1,2)
    min(5,2)
    print add.__name__
    
    
