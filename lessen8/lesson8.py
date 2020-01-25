import time
import psutil
import os


def time_func(func):
    def wapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Время исполнения функции {func.__name__}: {end_time-start_time} сек.')
        return result
    return wapper


def memory_func(func):
    def wapper(*args, **kwargs):
        proc = psutil.Process(os.getpid())
        start_memory = proc.memory_info().rss
        result = func(*args, **kwargs)
        end_memory = proc.memory_info().rss
        print(f"Физ. память используемая функцией {func.__name__}: {end_memory-start_memory} байт")
        return result
    return wapper


@memory_func
@time_func
def gen_list_nat(num):
    for i in range(num):
        yield i


@memory_func
@time_func
def list_nat(num):
    result = []
    for i in range(num):
        result.append(i)
    return result


gen_list_nat(10000000)
list_nat(10000000)
