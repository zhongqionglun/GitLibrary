# -*-coding:UTF-8-*-

"""
    装饰器-函数的装饰器，用于包装函数，使得调用前后能做根据包装器参数来打印不同的log信息
    
"""
from functools import wraps
import inspect, time


def advance_logger(loglevel):
    def get_line_number():
        return inspect.currentframe().f_back.f_back.f_lineno

    def _basic_log(fn, result, *args, **kwargs):
        print("function   = " + fn.__name__, end=' ')
        print("    arguments = {0} {1}".format(args, kwargs))
        print("    return    = {0}".format(result))

    def info_log_decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            result = fn(*args, **kwargs)
            _basic_log(fn, result, args, kwargs)

        return wrapper

    def debug_log_decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            ts = time.time()
            result = fn(*args, **kwargs)
            te = time.time()
            _basic_log(fn, result, args, kwargs)
            print("    time      = %.6f sec" % (te - ts))
            print("    called_from_line : " + str(get_line_number()))

        return wrapper

    if loglevel is "debug":
        return debug_log_decorator
    else:
        return info_log_decorator


@advance_logger('debug')
def fib(a, b):
    c = a + b
    if c > 100:
        return c
    fib(b, c)


if __name__ == "__main__":
    fib(0, 1)
