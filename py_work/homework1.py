# 编写一个Python程序，实现一个计数器函数，该函数能够记录特定函数的调用次数。你需要使用闭包和装饰器来实现这个功能。


def func_counter(func):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        res = func(*args, **kwargs)
        count += 1
        print('函数调用次数:{}'.format(count))
        return res

    return inner
